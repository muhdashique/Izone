# Generated by Django 4.2.2 on 2024-10-22 09:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('IZONapp', '0010_remove_galleryimage_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, related_name='products', to='IZONapp.categoryproduct'),
            preserve_default=False,
        ),
    ]
