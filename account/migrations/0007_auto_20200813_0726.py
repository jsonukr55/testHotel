# Generated by Django 2.0.7 on 2020-08-13 01:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_auto_20200813_0724'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='is_cutomer',
        ),
        migrations.RemoveField(
            model_name='account',
            name='is_hotel',
        ),
    ]
