# Generated by Django 4.2.2 on 2024-10-18 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IZONapp', '0002_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='product',
            name='stock',
        ),
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='product_images/'),
        ),
    ]