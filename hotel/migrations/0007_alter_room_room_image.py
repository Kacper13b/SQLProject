# Generated by Django 3.2.8 on 2021-11-02 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0006_room_room_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='room_image',
            field=models.ImageField(default='static/images/no.jpg', upload_to='media'),
        ),
    ]