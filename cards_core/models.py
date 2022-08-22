from django.db import models

# Create your models here.
class Card(models.Model):

    KIND_OF_BALL = [
        (1, 'Баскетбол'),
        (2, 'Волейбол'),
        (3, 'Футбол'),
    ]

    author = models.CharField(max_length=20, default='User')
    name = models.CharField(max_length=40)
    image = models.ImageField(upload_to='static')
    adress = models.CharField(max_length=60)
    work_hours = models.DurationField(null=True, blank=True, verbose_name='Время работы')
    kind_sport = models.PositiveSmallIntegerField(("Вид спорта"), choices=KIND_OF_BALL, blank=False, default=1)
    descr = models.TextField(max_length=500)

    def __str__(self):
        return f'{self.name} по адресу: {self.adress}'