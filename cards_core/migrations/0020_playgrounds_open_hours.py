# Generated by Django 4.1 on 2022-09-02 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards_core', '0019_remove_playgrounds_id_alter_playgrounds_adress'),
    ]

    operations = [
        migrations.AddField(
            model_name='playgrounds',
            name='open_hours',
            field=models.TextField(default='00:00-00:00', max_length=11, verbose_name='Время работы'),
        ),
    ]
