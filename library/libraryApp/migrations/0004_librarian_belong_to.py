# Generated by Django 2.2.6 on 2019-10-16 11:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('libraryApp', '0003_auto_20191016_1114'),
    ]

    operations = [
        migrations.AddField(
            model_name='librarian',
            name='belong_to',
            field=models.ForeignKey(help_text='Select library ID', null=True, on_delete=django.db.models.deletion.CASCADE, to='libraryApp.Libraries', verbose_name='Library ID'),
        ),
    ]
