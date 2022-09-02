from django.db import models


# Create your models here.
class Playgrounds(models.Model):

    KIND_OF_BALL = [
        ('Баскетбол', 'Баскетбол'),
        ('Волейбол', 'Волейбол'),
        ('Футбол', 'Футбол'),
    ]

    TYPE_OF_PG = [
        ('Открытый','Открытый'),
        ('Закрытый','Закрытый'),
    ]

    AVRG_CAPACITY = [
        ('0-50','0-50 человек'),
        ('50-100','50-100 человек'),
        ('+100','100+ человек'),
    ]

    adress = models.CharField(max_length=60, primary_key=True, verbose_name='Адрес площадки')
    kind_sport = models.CharField(("Вид спорта"), choices=KIND_OF_BALL, max_length=20)
    descr = models.TextField(max_length=500, verbose_name='Описание площадки')
    create_date = models.DateTimeField('Дата и время создания', auto_now_add=True)
    edit_date = models.DateTimeField('Дата и время изменения', auto_now=True)
    open_hours = models.TextField(max_length=11, verbose_name='Время работы', default='00:00-00:00')
    city = models.CharField(max_length=20, verbose_name='Город')
    type_pg = models.CharField(("Тип площадки"), choices=TYPE_OF_PG, max_length=20)
    coating = models.CharField(max_length=20, verbose_name='Покрытие')
    avrg_capacity = models.CharField(("Средняя вместимость"), choices=AVRG_CAPACITY, max_length=20)
    image = models.ImageField(upload_to='static', verbose_name='Фото площадки', default='')

    def __str__(self):
        return f'{self.kind_sport} по адресу: {self.adress}'

    class Meta:
        verbose_name = 'Площадка'
        verbose_name_plural = 'Площадки'

