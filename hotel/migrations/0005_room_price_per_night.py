# Generated by Django 3.2.8 on 2021-10-29 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0004_room_room_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='price_per_night',
            field=models.IntegerField(default=100),
            preserve_default=False,
        ),
    ]
