# Generated by Django 4.1.5 on 2023-02-04 18:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Наименование')),
                ('description', models.TextField(verbose_name='Описание')),
                ('image', models.ImageField(blank=True, null=True, upload_to='students/', verbose_name='Превью')),
                ('category', models.CharField(max_length=255, verbose_name='Категория')),
                ('price', models.IntegerField(verbose_name='Цена')),
                ('creation_date', models.DateTimeField(verbose_name='Дата создания')),
                ('date_last_modified', models.DateTimeField(verbose_name='Дата последнего изменения')),
                ('created_at', models.IntegerField(blank=True, null=True)),
                ('product_user', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Version',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('release_notes', models.CharField(max_length=255)),
                ('sign', models.BooleanField(default=True)),
                ('product', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='catalog.product')),
                ('product_user', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('name', models.CharField(max_length=255, primary_key=True, serialize=False, verbose_name='Наименование')),
                ('description', models.TextField(verbose_name='Описание')),
                ('product_user', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
