# Generated by Django 4.2.6 on 2023-10-28 10:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mailling', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Владелец'),
        ),
        migrations.AlterField(
            model_name='mailling',
            name='stop_to_send',
            field=models.TimeField(default=django.utils.timezone.now, verbose_name='Время окончания отправки'),
        ),
    ]
