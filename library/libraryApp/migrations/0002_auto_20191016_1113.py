# Generated by Django 2.2.6 on 2019-10-16 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libraryApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='libraries',
            name='id',
        ),
        migrations.AlterField(
            model_name='libraries',
            name='library_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
