# Generated by Django 4.2.2 on 2024-11-21 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IZONapp', '0009_product_category_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='brand_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='model_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
