from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import reverse
from PIL import Image

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
    title = models.CharField(max_length=256, unique=True, verbose_name='Название площадки')
    image = models.ImageField(upload_to='places', verbose_name='Фото площадки')
    kind_sport = models.CharField(("Вид спорта"), choices=KIND_OF_BALL, max_length=20)
    descr = models.TextField(verbose_name='Описание площадки')
    create_date = models.DateTimeField('Дата и время создания', auto_now_add=True)
    edit_date = models.DateTimeField('Дата и время изменения', auto_now=True)
    open_hours = models.TimeField('Часы открытия', default='00:00')
    close_hours = models.TimeField('Часы закрытия', default='00:00')
    city = models.CharField(max_length=20, verbose_name='Город', default='Минск')
    type_pg = models.CharField(("Тип площадки"), choices=TYPE_OF_PG, max_length=20)
    coating = models.CharField(max_length=20, verbose_name='Покрытие')

    def get_absolute_url(self, *args, **kwargs):
        return reverse('detail', kwargs={'pk': self.pk})

    def __str__(self):
        return f'{self.kind_sport} по адресу: {self.adress}'

    class Meta:
        verbose_name = 'Площадка'
        verbose_name_plural = 'Площадки'


class Review(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор отзыва')
    place = models.ForeignKey(Place, on_delete=models.CASCADE, verbose_name='Площадка')
    text = models.TextField(max_length=5000, verbose_name='Текст отзыва')
    create_data = models.DateTimeField('Дата отзыва', auto_now=True)

    def __str__(self):
        return f"{self.place.adress} - {self.author}"

    class Meta:
        ordering = ['-create_data']
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

# TODO переработать загружзгу изображений площадок
# class PhotoPlace(models.Model):
#     place = models.ForeignKey(Place, on_delete=models.CASCADE, verbose_name='Фото площадки')
#     title = models.CharField(max_length=100, verbose_name='Заголовок')
#     date = models.DateTimeField()
#     image = models.ImageField(upload_to='places', auto_now_add=True)
#
#     def __str__(self):
#         return self.title