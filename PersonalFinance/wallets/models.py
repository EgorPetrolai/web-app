from django.db import models


class Articles(models.Model):
    CHOICES = (
        ('BYN', 'BYN'),
        ('RUB', 'RUB'),
        ('USD', 'USD'),
        ('asd', 'USD'),
    )
    title = models.CharField('Название кошелька', max_length=20, default='')
    money = models.FloatField('Сумма', default=0)
    currency = models.CharField('Валюта', max_length=10, choices = CHOICES, default='')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Кошелек'
        verbose_name_plural = 'Кошельки'