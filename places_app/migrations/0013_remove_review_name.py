# Generated by Django 3.2 on 2022-09-09 18:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('places_app', '0012_remove_review_parent'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='name',
        ),
    ]
