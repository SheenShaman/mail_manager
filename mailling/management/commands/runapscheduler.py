import sys

from django.core.management import BaseCommand

from mailling.models import Mailling
from mailling.services import send_mailling
from config.mailling_scheduler import scheduler
from django.utils import timezone


def my_job():
    mailling = Mailling.objects.all()
    return send_mailling(mailling)


class Command(BaseCommand):
    # help = ""

    def handle(self, *args, **options):
        if Mailling.status:
            if Mailling.PERIOD == 'DAILY':
                return scheduler.add_job(my_job, 'interval', hours=24, name='send_mailling', jobstore='default')
            elif Mailling.PERIOD == 'WEEKLY':
                return scheduler.add_job(my_job, 'interval', hours=168, name='send_mailling', jobstore='default')
            elif Mailling.PERIOD == 'MONTHLY':
                return scheduler.add_job(my_job, 'interval', hours=720, name='send_mailling', jobstore='default')
            scheduler.start()
            print("Scheduler started...", file=sys.stdout)
        elif Mailling.status is False:
            scheduler.pause()

        if Mailling.time_to_end == timezone.now():
            scheduler.pause_job(my_job())


# def start():
#     if Mailling.status:
#         if Mailling.PERIOD == 'DAILY':
#             return scheduler.add_job(my_job, 'interval', hours=24, name='send_mailings', jobstore='default')
#         elif Mailling.PERIOD == 'WEEKLY':
#             return scheduler.add_job(my_job, 'interval', day=168, name='send_mailings', jobstore='default')
#         elif Mailling.PERIOD == 'MONTHLY':
#             return scheduler.add_job(my_job, 'interval', hours=720, name='send_mailings', jobstore='default')
#         scheduler.start()
#         print("Scheduler started...", file=sys.stdout)
#     elif Mailling.status is False:
#         scheduler.pause()
#
#     if Mailling.time_to_end == timezone.now():
#         scheduler.pause_job(my_job())
