# Generated by Django 4.1 on 2022-08-27 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards_core', '0010_delete_mode'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата и время создания')),
                ('edit_date', models.DateTimeField(auto_now=True, verbose_name='Дата и время изменения')),
            ],
        ),
    ]