# Generated by Django 2.0.7 on 2020-08-13 01:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_auto_20200813_0713'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='is_cutomer',
            field=models.BooleanField(default=False, verbose_name='is cutomer'),
        ),
        migrations.AddField(
            model_name='account',
            name='is_hotel',
            field=models.BooleanField(default=False, verbose_name='is hotel'),
        ),
    ]