from django.db import models


# Create your models here.
class Playground(models.Model):

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

    author = models.CharField(max_length=20, default='User', verbose_name='Автор')
    image = models.ImageField(upload_to='static', verbose_name='Фото площадки')
    adress = models.CharField(max_length=60, verbose_name='Адрес площадки')
    kind_sport = models.CharField(("Вид спорта"), choices=KIND_OF_BALL, blank=True, default='', max_length=20)
    descr = models.TextField(max_length=500, verbose_name='Описание площадки')
    create_date = models.DateTimeField('Дата и время создания',auto_now_add=True)
    edit_date = models.DateTimeField('Дата и время изменения',auto_now=True)
    city = models.CharField(max_length=20, verbose_name='Город', default='')
    type_pg = models.CharField(("Тип площадки"), choices=TYPE_OF_PG, blank=True, default='', max_length=20)
    coating = models.CharField(max_length=20, verbose_name='Покрытие', default='')
    avrg_capacity = models.CharField(("Средняя вместимость"), choices=AVRG_CAPACITY, blank=True, default='', max_length=20)

    def __str__(self):
        return f'{self.kind_sport} по адресу: {self.adress}'

    class Meta:
        verbose_name = 'Площадка'
        verbose_name_plural = 'Площадки'
