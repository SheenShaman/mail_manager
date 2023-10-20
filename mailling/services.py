from datetime import datetime
from smtplib import SMTPException
from django.core.mail import send_mail
from mailling.models import Logs, Mailling
from django.conf import settings


def send_mailling(mailling):
    for client in mailling.client.all():
        try:
            send_mail(
                mailling.message.head,
                mailling.message.body,
                settings.EMAIL_HOST_USER,
                recipient_list=[client],
                fail_silently=False
            )
            log = Logs.objects.create(
                last_try=mailling.time_to_start,
                status_try='Успешно',
                mailling=mailling,
                client=client.email
            )
            log.save()
            return log

        except SMTPException as error:
            log = Logs.objects.create(
                last_try=mailling.time_to_start,
                status_try='Ошибка',
                mailling=mailling,
                client=client.email,
                answer=error
            )
            log.save()
            return log


def task():

    daily = 'DAILY'
    weekly = 'WEEKLY'
    monthly = 'MONTHLY'

    for m in Mailling.objects.all().filter(
        time_to_start=datetime.now().time().hour + 1,
        time_to_end=datetime.now().time().hour,
        periodicity=daily,
        status=True
    ):
        send_mailling(m)

    for m in Mailling.objects.all().filter(
        time_to_start=datetime.now().time().hour + 1,
        time_to_end=datetime.now().time().hour,
        periodicity=weekly,
        status=True
    ):
        send_mailling(m)
