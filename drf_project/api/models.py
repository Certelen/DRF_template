from django.db import models


class Ad(models.Model):
    title = models.CharField(
        'Заголовок объявления',
        max_length=200
    )
    id_number = models.PositiveIntegerField(
        'id объявления'
    )
    author = models.CharField(
        'Автор объявления',
        max_length=200
    )
    viewing = models.PositiveIntegerField(
        'Просмотры объявления'
    )
    position = models.PositiveIntegerField(
        'Позиция объявления'
    )

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'

    def __str__(self):
        return f'Объявление {self.title} от {self.author}'


class Check(models.Model):
    last_check = models.DateTimeField(
        'Дата последней проверки',
        auto_now_add=True
    )

    class Meta:
        verbose_name = 'Запрос к сайту'
        verbose_name_plural = 'Запросы к сайту'

    def __str__(self):
        return f'Запрос от {self.last_check}'
