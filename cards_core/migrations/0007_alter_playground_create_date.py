# Generated by Django 4.1 on 2022-08-27 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards_core', '0006_remove_playground_name_alter_playground_create_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='playground',
            name='create_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата b время создания'),
        ),
    ]
