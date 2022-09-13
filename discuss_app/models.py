from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import reverse

# Create your models here.

class Discuss(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')
    title = models.CharField(max_length=32, verbose_name='Название темы')
    text = models.TextField(max_length=5000, verbose_name='Главный текст темы')
    edit_date = models.DateTimeField(auto_now=True, verbose_name='Дата добавления')

    def get_absolute_url(self, *args, **kwargs):
        return reverse('detail-discuss', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = 'Тема обсуждения'
        verbose_name_plural = 'Темы обсуждения'

    def __str__(self):
        return f'{self.title} - {self.author}'


class DiscussText(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')
    discuss = models.ForeignKey(Discuss, on_delete=models.CASCADE, verbose_name='Тема')
    text = models.TextField(max_length=5000, verbose_name='Текст юзера')
    edit_date = models.DateTimeField(auto_now=True, verbose_name='Дата добавления')

    class Meta:
        verbose_name = 'Текст обсуждения'
        verbose_name_plural = 'Текста обсуждения'

    def __str__(self):
        return f'{self.discuss}'