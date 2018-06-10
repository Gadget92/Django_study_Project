from django.db import models

class PizzaShop(models.Model):
    name = models.CharField(max_length=30, verbose_name='Пиццерия')
    description = models.TextField(verbose_name='Описание')
    rating = models.FloatField(default=0, verbose_name='Рейтинг')
    url = models.URLField(verbose_name='Интернет адрес')

    class Meta:
        verbose_name = 'Пиццерия'
        verbose_name_plural = 'Пиццерии'

    def __str__(self):
        return self.name


class Pizza(models.Model):
    pizza_shop = models.ForeignKey(PizzaShop, on_delete=models.CASCADE, verbose_name='Пиццерия')
    name = models.CharField(max_length=30, verbose_name='Название пиццы')
    short_description = models.CharField(max_length=30, verbose_name='Краткое описание')
    price = models.FloatField(default=0, verbose_name='Цена')

    class Meta:
        ordering = ['name']
        verbose_name = 'Пицца'
        verbose_name_plural = 'Пиццы'


    def __str__(self):
        return self.name