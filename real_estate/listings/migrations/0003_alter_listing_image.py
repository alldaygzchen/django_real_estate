# Generated by Django 4.1.5 on 2023-01-22 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0002_listing_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='image',
            field=models.ImageField(default='', upload_to='media'),
        ),
    ]
