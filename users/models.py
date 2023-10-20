from django.contrib.auth.models import AbstractUser
from django.db import models

from mailling.models import NULLABLE


class User(AbstractUser):
    username = None

    email = models.EmailField(unique=True, verbose_name='Email')
    fio = models.CharField(max_length=100, verbose_name='ФИО', **NULLABLE)

    is_active = models.BooleanField(verbose_name='активный пользователь', default=False)
    verify_code = models.CharField(max_length=50, verbose_name='Верификация')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
