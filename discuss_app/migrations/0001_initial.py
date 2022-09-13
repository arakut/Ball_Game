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
            name='Discuss',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32, verbose_name='Название темы')),
                ('text', models.TextField(max_length=5000, verbose_name='Главный текст темы')),
                ('edit_date', models.DateTimeField(auto_now=True, verbose_name='Дата добавления')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
            ],
            options={
                'verbose_name': 'Тема обсуждения',
                'verbose_name_plural': 'Темы обсуждения',
            },
        ),
        migrations.CreateModel(
            name='DiscussText',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=5000, verbose_name='Текст юзера')),
                ('edit_date', models.DateTimeField(auto_now=True, verbose_name='Дата добавления')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
                ('discuss', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='discuss_app.discuss', verbose_name='Тема')),
            ],
            options={
                'verbose_name': 'Текст обсуждения',
                'verbose_name_plural': 'Текста обсуждения',
            },
        ),
    ]