from django.db import models


# Create your models here.
class Playground(models.Model):

    KIND_OF_BALL = [
        ('Баскетбол', 'Баскетбол'),
        ('Волейбол', 'Волейбол'),
        ('Футбол', 'Футбол'),
    ]

    author = models.CharField(max_length=20, default='User', verbose_name='Автор')
    image = models.ImageField(upload_to='static', verbose_name='Фото площадки')
    adress = models.CharField(max_length=60, verbose_name='Адрес площадки')
    kind_sport = models.CharField(("Вид спорта"), choices=KIND_OF_BALL, blank=True, default='Басктебол', max_length=20)
    descr = models.TextField(max_length=500, verbose_name='Описание площадки')
    create_date = models.DateTimeField('Дата и время создания',auto_now_add=True)
    edit_date = models.DateTimeField('Дата и время изменения',auto_now=True)

    def __str__(self):
        return f'{self.kind_sport} по адресу: {self.adress}'
