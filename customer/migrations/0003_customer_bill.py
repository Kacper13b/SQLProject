# Generated by Django 3.2.8 on 2021-11-08 21:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0002_additionalservice_bill'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='bill',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to='customer.bill'),
            preserve_default=False,
        ),
    ]
