# Generated by Django 2.0.6 on 2018-06-09 21:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0002_pizza'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pizza',
            name='pizza_shop',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='firstapp.PizzaShop', verbose_name='Пиццерия'),
        ),
        migrations.AlterField(
            model_name='pizza',
            name='price',
            field=models.FloatField(default=0, verbose_name='Цена'),
        ),
    ]
