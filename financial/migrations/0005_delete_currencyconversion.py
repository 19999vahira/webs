# Generated by Django 5.0.4 on 2024-04-24 21:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('financial', '0004_currencyconversion'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CurrencyConversion',
        ),
    ]
