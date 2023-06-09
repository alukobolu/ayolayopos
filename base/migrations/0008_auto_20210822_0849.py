# Generated by Django 3.1.2 on 2021-08-22 07:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_atm_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='atm',
            name='date',
            field=models.DateField(default=datetime.date(2021, 8, 22), null=True),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='picture',
            field=models.ImageField(blank=True, default='avatar.png', upload_to='inventory/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='date',
            field=models.DateField(default=datetime.date(2021, 8, 22), null=True),
        ),
    ]
