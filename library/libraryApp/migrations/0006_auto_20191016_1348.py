# Generated by Django 2.2.6 on 2019-10-16 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libraryApp', '0005_auto_20191016_1304'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='returned_date',
            field=models.DateField(help_text='Enter if book returned', null=True, verbose_name='Returned date'),
        ),
    ]