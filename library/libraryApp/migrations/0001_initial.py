# Generated by Django 2.2.6 on 2019-10-16 11:10

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_name', models.CharField(help_text='Enter author name', max_length=100, verbose_name='Author')),
                ('about_author', models.TextField(help_text='Write something about author', verbose_name='About')),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isbn', models.IntegerField(help_text='Enter ISBN number for book', verbose_name='ISBN')),
                ('book_name', models.CharField(help_text='Enter book name', max_length=100, verbose_name='Name')),
                ('category', models.CharField(default=None, help_text='Enter the category of book', max_length=100, verbose_name='Category')),
                ('number_of_copy', models.IntegerField(default=1, help_text='Enter the number of copies available', verbose_name='Book count')),
                ('stock', models.IntegerField(default=1, help_text='Enter the Book available', verbose_name='Stock')),
                ('availability', models.BooleanField(default=True)),
                ('description', models.TextField(help_text='Write something about book', null=True, verbose_name='Description')),
                ('price', models.IntegerField(default=0, help_text='Enter the price of book', verbose_name='Price')),
                ('book_author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='libraryApp.Author')),
            ],
        ),
        migrations.CreateModel(
            name='Librarian',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('librarian_ID', models.IntegerField(help_text='Enter Librarian ID', verbose_name='ID')),
                ('librarian_name', models.CharField(help_text='Enter Librarian Name', max_length=100, verbose_name='Name')),
                ('librarian_contact_no', models.IntegerField(help_text='Enter Librarian contact number', verbose_name='Phone number')),
            ],
        ),
        migrations.CreateModel(
            name='Libraries',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('library_id', models.IntegerField(help_text='Enter library ID', verbose_name='ID')),
                ('library_address', models.TextField(help_text='Enter library address', verbose_name='Address')),
                ('library_contact_number', models.IntegerField(help_text='Enter library contact number', verbose_name='Phone number')),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('member_ID', models.IntegerField(help_text='Enter member ID', verbose_name='ID')),
                ('member_name', models.CharField(help_text='Enter member name', max_length=100, verbose_name='Name')),
                ('member_contact_number', models.IntegerField(help_text='Enter member phone number', verbose_name='Phone number')),
                ('member_email', models.EmailField(help_text='Enter member Email', max_length=254, verbose_name='Email')),
                ('member_address', models.TextField(help_text='Enter member address', null=True, verbose_name='Address')),
            ],
        ),
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('borrowed_ID', models.IntegerField(auto_created=True)),
                ('issue_date', models.DateField(auto_now_add=True, verbose_name='Issued Date')),
                ('return_date', models.DateField(default=datetime.date(2019, 10, 23), help_text='Enter return date', verbose_name='Return date')),
                ('is_return', models.BooleanField(default=False, help_text='Select if book is returning', verbose_name='Return')),
                ('returned_date', models.DateField(help_text='Enter if book returned', verbose_name='Returned date')),
                ('borrowed_book', models.ForeignKey(help_text='Select Book name', on_delete=django.db.models.deletion.CASCADE, to='libraryApp.Book', verbose_name='Book name')),
                ('borrowed_member', models.ForeignKey(help_text='Select Member name', on_delete=django.db.models.deletion.CASCADE, to='libraryApp.Member', verbose_name='Member name')),
                ('issued_librarian', models.ForeignKey(help_text='Select librarian', on_delete=django.db.models.deletion.CASCADE, to='libraryApp.Librarian', verbose_name='Issued Librarian')),
            ],
        ),
    ]
