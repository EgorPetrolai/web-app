# Generated by Django 5.0 on 2023-12-28 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wallets', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='articles',
            options={'verbose_name': 'Кошелек', 'verbose_name_plural': 'Кошельки'},
        ),
        migrations.RemoveField(
            model_name='articles',
            name='subtitle',
        ),
        migrations.AddField(
            model_name='articles',
            name='currency',
            field=models.CharField(choices=[('BYN', 'BYN'), ('RUB', 'RUB'), ('USD', 'USD')], default='', max_length=10, verbose_name='Валюта'),
        ),
        migrations.AddField(
            model_name='articles',
            name='money',
            field=models.FloatField(default=0, verbose_name='Сумма'),
        ),
    ]