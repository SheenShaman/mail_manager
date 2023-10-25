from mailling.services import send_mailling
from datetime import datetime
from mailling.models import Mailling


def tasks():
    current_time = datetime.now()
    mailings = Mailling.objects.filter(time_to_send=current_time)
    if mailings.exists():
        for mailing in mailings:
            send_mailling(mailing)


def daily_tasks():
    mailings = Mailling.objects.filter(periodicity="DAILY")
    if mailings.exists():
        for mailing in mailings:
            send_mailling(mailing)


def weekly_tasks():
    mailings = Mailling.objects.filter(periodicity="WEEKLY")
    if mailings.exists():
        for mailing in mailings:
            send_mailling(mailing)


def monthly_tasks():
    mailings = Mailling.objects.filter(periodicity="MONTHLY")
    if mailings.exists():
        for mailing in mailings:
            send_mailling(mailing)
