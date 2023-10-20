from django.contrib import admin

from mailling.models import Mailling, Message, Client, Logs


@admin.register(Mailling)
class MaillingAdmin(admin.ModelAdmin):
    list_display = ('time_to_start', 'time_to_end', 'periodicity', 'status',)
    list_filter = ('status', 'periodicity',)


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('head', 'body',)
    search_fields = ('head', 'body',)


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('email', 'fio',)
    search_fields = ('email', 'fio',)


@admin.register(Logs)
class LogsAdmin(admin.ModelAdmin):
    list_display = ('last_try', 'status_try',)
    list_filter = ('status_try',)
