# Generated by Django 3.2.8 on 2021-11-02 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0005_alter_room_hotel'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='room_image',
            field=models.ImageField(default='static/images/logo.png', upload_to='media'),
        ),
    ]
