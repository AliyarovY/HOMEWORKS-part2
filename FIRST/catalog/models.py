from django.db import models


NULLABLE = dict(blank=True, null=True)


class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание')
    image = models.ImageField(upload_to='students/', **NULLABLE, verbose_name='Превью')
    category = models.CharField(max_length=255, verbose_name='Категория')
    price = models.IntegerField(verbose_name='Цена')
    creation_date = models.DateTimeField(verbose_name='Дата создания')
    date_last_modified = models.DateTimeField(verbose_name='Дата последнего изменения')
    created_at = models.IntegerField(**NULLABLE)


class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='Наименование', primary_key=True)
    description = models.TextField(verbose_name='Описание')
