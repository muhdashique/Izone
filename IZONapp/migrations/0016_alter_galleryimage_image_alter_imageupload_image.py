# Generated by Django 4.2.2 on 2024-10-23 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IZONapp', '0015_remove_product_category_delete_categoryproduct'),
    ]

    operations = [
        migrations.AlterField(
            model_name='galleryimage',
            name='image',
            field=models.ImageField(upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='imageupload',
            name='image',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
