# Generated by Django 4.2.6 on 2023-10-07 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='comment',
        ),
        migrations.AlterField(
            model_name='user',
            name='fio',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='ФИО'),
        ),
    ]