from django.utils import timezone

from django.db import models

from config import settings

NULLABLE = {'null': True, 'blank': True}


class Mailling(models.Model):
    PERIOD = (
        ('DAILY', 'Каждый день'),
        ('WEEKLY', 'Каждую неделю'),
        ('MONTHLY', 'Каждый месяц'),
    )

    start_to_send = models.TimeField(verbose_name='Время начало отправки', default=timezone.now)
    stop_to_send = models.TimeField(verbose_name='Время окончания отправки', default=timezone.now)
    periodicity = models.CharField(max_length=50, verbose_name='Периодичность', choices=PERIOD)
    is_active = models.BooleanField(max_length=20, verbose_name='Пуск рассылки', default=False)

    client = models.ManyToManyField('Client', verbose_name='Кому')
    message = models.ForeignKey('Message', on_delete=models.CASCADE, verbose_name='Сообщение')
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Пользователь', **NULLABLE
    )

    def __str__(self):
        return f'{self.start_to_send}-{self.stop_to_send} {self.periodicity} {self.is_active} {self.client} {self.message}'

    class Meta:
        verbose_name = "Настройка"
        verbose_name_plural = "Настройки"


class Message(models.Model):
    head = models.CharField(max_length=100, verbose_name='Тема')
    body = models.TextField(verbose_name='Сообщение')

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Пользователь', **NULLABLE
    )

    def __str__(self):
        return f'{self.head} {self.body}'

    class Meta:
        verbose_name = "Сообщение"
        verbose_name_plural = "Сообщения"


class Client(models.Model):
    email = models.EmailField(unique=True, verbose_name='Email')
    fio = models.CharField(max_length=100, verbose_name='ФИО', **NULLABLE)
    comment = models.TextField(verbose_name='Комментарий', **NULLABLE)

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Владелец', **NULLABLE
    )

    def __str__(self):
        return f'{self.email}'

    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"


class Logs(models.Model):
    STATUSES = (
        ('OK', 'Успешно'),
        ('FAILED', 'Ошибка'),
    )

    last_try = models.DateTimeField(verbose_name='Время последней попытки', auto_now_add=True)
    status_try = models.CharField(max_length=50, choices=STATUSES, verbose_name='Статус попытки', default='Успешно')
    answer = models.CharField(max_length=250, verbose_name='Ответ сервера', **NULLABLE)

    mailling = models.ForeignKey(Mailling, on_delete=models.CASCADE, verbose_name='Рассылка')
    client = models.EmailField(max_length=150, verbose_name='Email клиента', **NULLABLE)

    def __str__(self):
        return f'{self.last_try} {self.status_try} {self.mailling} {self.client}'

    class Meta:
        verbose_name = "Лог"
        verbose_name_plural = "Логи"
