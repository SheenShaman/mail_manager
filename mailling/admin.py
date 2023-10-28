from django.contrib import admin

from mailling.models import Mailling, Message, Client, Logs


admin.site.register(Client)
admin.site.register(Logs)
admin.site.register(Message)
admin.site.register(Mailling)
