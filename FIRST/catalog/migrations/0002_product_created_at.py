# Generated by Django 4.1.5 on 2023-01-18 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='created_at',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]