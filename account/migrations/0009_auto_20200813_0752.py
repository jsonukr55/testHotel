# Generated by Django 2.0.7 on 2020-08-13 02:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0008_auto_20200813_0734'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='account_type',
            field=models.CharField(choices=[('hotel', 'Hotel'), ('customer', 'Customer')], default=False, max_length=1, verbose_name='account_type'),
        ),
    ]