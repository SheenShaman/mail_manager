from django.apps import AppConfig


class MaillingConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'mailling'

    # def ready(self):
    #     from mailling.scheduler import runapscheduler
    #     runapscheduler.start()
