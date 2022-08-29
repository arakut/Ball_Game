# Generated by Django 4.1 on 2022-08-29 19:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cards_core', '0013_delete_mode_playground_avrg_capacity_playground_city_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='playground',
            name='avrg_capacity',
            field=models.CharField(blank=True, choices=[('0-50', '0-50 человек'), ('50-100', '50-100 человек'), ('+100', '100+ человек')], default='', max_length=20, verbose_name='Средняя вместимость'),
        ),
        migrations.AlterField(
            model_name='playground',
            name='city',
            field=models.CharField(default='', max_length=20, verbose_name='Город'),
        ),
        migrations.AlterField(
            model_name='playground',
            name='coating',
            field=models.CharField(default='', max_length=20, verbose_name='Покрытие'),
        ),
        migrations.AlterField(
            model_name='playground',
            name='kind_sport',
            field=models.CharField(blank=True, choices=[('Баскетбол', 'Баскетбол'), ('Волейбол', 'Волейбол'), ('Футбол', 'Футбол')], default='', max_length=20, verbose_name='Вид спорта'),
        ),
        migrations.AlterField(
            model_name='playground',
            name='type_pg',
            field=models.CharField(blank=True, choices=[('Открытый', 'Открытый'), ('Закрытый', 'Закрытый')], default='', max_length=20, verbose_name='Тип площадки'),
        ),
        migrations.CreateModel(
            name='Home_Radnom_Pg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adress', models.CharField(max_length=60, verbose_name='Адрес площадки')),
                ('pg_pic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cards_core.playground')),
            ],
        ),
    ]
