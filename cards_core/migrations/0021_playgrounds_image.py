# Generated by Django 4.1 on 2022-09-02 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards_core', '0020_playgrounds_open_hours'),
    ]

    operations = [
        migrations.AddField(
            model_name='playgrounds',
            name='image',
            field=models.ImageField(default='', upload_to='static', verbose_name='Фото площадки'),
        ),
    ]