# Generated by Django 5.1.1 on 2024-10-16 06:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotelapp', '0007_room_room_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='date_of_check_in',
            field=models.DateField(default=datetime.date.today),
        ),
    ]