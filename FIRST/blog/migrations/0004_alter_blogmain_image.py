# Generated by Django 4.1.5 on 2023-01-22 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_blogmain_options_alter_blogmain_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogmain',
            name='image',
            field=models.ImageField(blank=True, upload_to='photos/%Y/%m/%d'),
        ),
    ]
