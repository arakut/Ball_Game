# Generated by Django 3.2 on 2022-09-07 23:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places_app', '0007_alter_place_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='image',
            field=models.ImageField(default='default_place.png', upload_to='places', verbose_name='Фото площадки'),
        ),
    ]
