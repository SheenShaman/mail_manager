from datetime import datetime, timezone
from smtplib import SMTPException
from django.core.mail import send_mail
from mailling.models import Logs, Mailling, Client, Message
from django.conf import settings
from django.core.cache import cache


def get_cache_clients():
    if settings.CACHE_ENABLED:
        key = 'client_list'
        client_list = cache.get(key)
        if client_list is None:
            client_list = Client.objects.all()
            cache.set(key, client_list)
    else:
        client_list = Client.objects.all()
    return client_list


def get_cache_messages():
    if settings.CACHE_ENABLED:
        key = 'message_list'
        message_list = cache.get(key)
        if message_list is None:
            message_list = Message.objects.all()
            cache.set(key, message_list)
    else:
        message_list = Message.objects.all()
    return message_list


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
                last_try=mailling.time_to_send,
                status_try='Успешно',
                mailling=mailling,
                client=client.email
            )
            log.save()
            return log

        except SMTPException as error:
            log = Logs.objects.create(
                last_try=mailling.time_to_send,
                status_try='Ошибка',
                mailling=mailling,
                client=client.email,
                answer=error
            )
            log.save()
            return log
