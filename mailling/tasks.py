from mailling.services import send_mailling
from mailling.models import Mailling


def daily_tasks():
    mailings = Mailling.objects.filter(periodicity="DAILY", status=True)
    if mailings.exists():
        for mailing in mailings:
            send_mailling(mailing)


def weekly_tasks():
    mailings = Mailling.objects.filter(periodicity="WEEKLY", status=True)
    if mailings.exists():
        for mailing in mailings:
            send_mailling(mailing)


def monthly_tasks():
    mailings = Mailling.objects.filter(periodicity="MONTHLY", status=True)
    if mailings.exists():
        for mailing in mailings:
            send_mailling(mailing)
