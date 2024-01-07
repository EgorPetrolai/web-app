from django.db import models


class Articles(models.Model):
    title = models.CharField('Заголовок', max_length=50, default='')
    subtitle = models.CharField('описание', max_length=50, default='')
    fulltext = models.CharField('Текст новости', max_length=200, default='')
    date = models.CharField('Дата', max_length=10, default='')
    time = models.CharField('Время', max_length=10, default='')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'