from django.db import models

# Create your models here.
class Playground(models.Model):

    KIND_OF_BALL = [
        ('Баскетбол', 'Баскетбол'),
        ('Волейбол', 'Волейбол'),
        ('Футбол', 'Футбол'),
    ]

    author = models.CharField(max_length=20, default='User', verbose_name='Автор')
    name = models.CharField(max_length=40)
    image = models.ImageField(upload_to='static', verbose_name='Фото площадки')
    adress = models.CharField(max_length=60, verbose_name='Адрес площадки')
    open_hours = models.TimeField(auto_now=False, auto_now_add=False)
    close_hours = models.TimeField(default='00:00')
    kind_sport = models.CharField(("Вид спорта"), choices=KIND_OF_BALL, blank=True, default='Басктебол', max_length=20)
    descr = models.TextField(max_length=500, verbose_name='Описание площадки')

    def __str__(self):
        return f'{self.name} по адресу: {self.adress}'