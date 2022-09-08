from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=10, default='Имя', verbose_name='Имя пользователя')
    image = models.ImageField(default='default.png', upload_to='profile_pics', verbose_name='Фото пользователя')
    age = models.IntegerField(default=0, verbose_name='Возраст пользователя')
    registr_date = models.DateTimeField('Дата регистрации пользователя', auto_now_add=True)
    telegarm = models.CharField(max_length=32, default='@', verbose_name='Ник в телеграме')
    social_urls = models.CharField(max_length=32, default='-', verbose_name='Ссылки на соц. сети')

    def __str__(self):
        return f'{self.user.username} Profile'