# Generated by Django 3.1.2 on 2021-08-19 20:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_atm_other_info'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='date',
            field=models.DateField(default=datetime.date(2021, 8, 19), null=True),
        ),
    ]
