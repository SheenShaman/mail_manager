from django.conf import settings
from django.core.mail import send_mail

from users.models import User


def send_verify_code(user: User, url):
    send_mail(
        'Подтверждение регистрации',
        f'Чтобы подтвердить регистрацию перейдите по ссылке {url}',
        settings.EMAIL_HOST_USER,
        [user.email]
    )


def send_password(email, password):
    send_mail(
        'Сброс пароля',
        f'Вы сбросили пароль. Ваш новый пароль {password}',
        settings.EMAIL_HOST_USER,
        [email]
    )
