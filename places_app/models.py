from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import  reverse

class Place(models.Model):

    KIND_OF_BALL = [
        ('Баскетбол', 'Баскетбол'),
        ('Волейбол', 'Волейбол'),
        ('Футбол', 'Футбол'),
    ]

    TYPE_OF_PG = [
        ('Открытый', 'Открытый'),
        ('Закрытый', 'Закрытый'),
    ]

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    adress = models.CharField(max_length=60, unique=True, verbose_name='Адрес площадки')
    image = models.ImageField(upload_to='places', verbose_name='Фото площадки')
    kind_sport = models.CharField(("Вид спорта"), choices=KIND_OF_BALL, max_length=20)
    descr = models.TextField(verbose_name='Описание площадки')
    create_date = models.DateTimeField('Дата и время создания', auto_now_add=True)
    edit_date = models.DateTimeField('Дата и время изменения', auto_now=True)
    open_hours = models.TimeField(default='00:00')
    close_hours = models.TimeField(default='00:00')
    city = models.CharField(max_length=20, verbose_name='Город', default='Минск')
    type_pg = models.CharField(("Тип площадки"), choices=TYPE_OF_PG, max_length=20)
    coating = models.CharField(max_length=20, verbose_name='Покрытие')

    def get_absolute_url(self, *args, **kwargs):
        return reverse('detail', kwargs={'pk': self.pk})

    def __str__(self):
        return f'{self.kind_sport} по адресу: {self.adress}'