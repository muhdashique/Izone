# Generated by Django 4.2.2 on 2024-11-18 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IZONapp', '0008_alter_product_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category_image',
            field=models.ImageField(blank=True, null=True, upload_to='category_images/'),
        ),
    ]
