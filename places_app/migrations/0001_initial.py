# Generated by Django 3.2 on 2022-09-13 13:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adress', models.CharField(max_length=60, unique=True, verbose_name='Адрес площадки')),
                ('title', models.CharField(max_length=60, unique=True, verbose_name='Название площадки')),
                ('image', models.ImageField(upload_to='places', verbose_name='Фото площадки')),
                ('kind_sport', models.CharField(choices=[('Баскетбол', 'Баскетбол'), ('Волейбол', 'Волейбол'), ('Футбол', 'Футбол')], max_length=20, verbose_name='Вид спорта')),
                ('descr', models.TextField(verbose_name='Описание площадки')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата и время создания')),
                ('edit_date', models.DateTimeField(auto_now=True, verbose_name='Дата и время изменения')),
                ('open_hours', models.TimeField(default='00:00')),
                ('close_hours', models.TimeField(default='00:00')),
                ('city', models.CharField(default='Минск', max_length=20, verbose_name='Город')),
                ('type_pg', models.CharField(choices=[('Открытый', 'Открытый'), ('Закрытый', 'Закрытый')], max_length=20, verbose_name='Тип площадки')),
                ('coating', models.CharField(max_length=20, verbose_name='Покрытие')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Площадка',
                'verbose_name_plural': 'Площадки',
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=5000, verbose_name='Текст отзыва')),
                ('create_data', models.DateTimeField(auto_now=True, verbose_name='Дата отзыва')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор отзыва')),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='places_app.place', verbose_name='Площадка')),
            ],
            options={
                'verbose_name': 'Отзыв',
                'verbose_name_plural': 'Отзывы',
                'ordering': ['-create_data'],
            },
        ),
    ]
