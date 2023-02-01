from django.db import models
from django.core.exceptions import ValidationError
from users.models import User


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
    product_user = models.ForeignKey(User, default=None, **NULLABLE, on_delete=models.SET_NULL)


class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='Наименование', primary_key=True)
    description = models.TextField(verbose_name='Описание')
    product_user = models.ForeignKey(User, default=None, **NULLABLE, on_delete=models.SET_NULL)


active_versions = set()


class Version(models.Model):
    product = models.OneToOneField('Product', on_delete=models.CASCADE)
    number = models.IntegerField()
    release_notes = models.CharField(max_length=255)
    sign = models.BooleanField(default=True)
    product_user = models.ForeignKey(User, default=None, **NULLABLE, on_delete=models.SET_NULL)


    def save(self, *args, **kwargs):
        if self.product in active_versions:
            raise ValidationError('product have active version')
        if self.sign:
            active_versions.add(self.product)

        return super().save(*args, **kwargs)
