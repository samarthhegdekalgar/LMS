# Generated by Django 2.2.6 on 2019-10-17 03:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libraryApp', '0015_auto_20191017_0342'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='return_date',
            field=models.DateField(default=datetime.date(2019, 10, 24), help_text='Enter return date', verbose_name='Return date'),
        ),
    ]
