# Generated by Django 2.2.6 on 2019-10-17 03:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libraryApp', '0016_auto_20191017_0344'),
    ]

    operations = [
        migrations.AddField(
            model_name='record',
            name='penalty',
            field=models.IntegerField(default=0, help_text='Enter in rupee', verbose_name='Penalty'),
        ),
    ]