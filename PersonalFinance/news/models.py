from django.db import models
from django.contrib.auth.models import User

class Article(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField('Заголовок', max_length=100, default='')
    subtitle = models.CharField('Описание', max_length=100, default='')
    fulltext = models.CharField('Текст новости', max_length=2000, default='')
    date = models.DateField('Дата')
    time = models.TimeField('Время')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
