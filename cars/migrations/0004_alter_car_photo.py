# Generated by Django 5.0.2 on 2024-03-14 00:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0003_car_photo_car_plate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='photo',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='cars/'),
        ),
    ]
