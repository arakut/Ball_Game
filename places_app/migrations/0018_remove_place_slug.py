# Generated by Django 3.2 on 2022-09-10 22:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('places_app', '0017_place_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='place',
            name='slug',
        ),
    ]
