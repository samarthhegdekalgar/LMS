from django.db import models
from datetime import date, timedelta
from django.db.models import signals
from django.dispatch import receiver


class Libraries(models.Model):
    library_id = models.AutoField(primary_key=True, verbose_name='ID')
    library_address = models.TextField(verbose_name='Address', help_text='Enter library address')
    library_contact_number = models.IntegerField(verbose_name='Phone number', help_text='Enter library contact number')

    def __str__(self):
        return str(self.library_id)


class Librarian(models.Model):
    librarian_ID = models.AutoField(primary_key=True, verbose_name='Employee ID')
    librarian_name = models.CharField(verbose_name='Name', max_length=100, help_text='Enter Librarian Name')
    librarian_contact_no = models.IntegerField(verbose_name='Phone number', help_text='Enter Librarian contact number')
    belong_to = models.ForeignKey(Libraries, verbose_name='Library ID', help_text='Select library ID',
                                  on_delete=models.CASCADE, null=True)

    def __str__(self):
        return str(self.librarian_ID)


class Author(models.Model):
    author_name = models.CharField(verbose_name='Author', max_length=100, help_text='Enter author name')
    about_author = models.TextField(verbose_name='About', help_text='Write something about author')

    def __str__(self):
        return self.author_name


class Book(models.Model):
    isbn = models.IntegerField(verbose_name='ISBN', help_text='Enter ISBN number for book')
    book_name = models.CharField(verbose_name='Name', max_length=100, help_text='Enter book name')
    category = models.CharField(verbose_name='Category', default=None, help_text='Enter the category of book',
                                max_length=100)
    number_of_copy = models.IntegerField(verbose_name='Book count', default=1, help_text='Enter the number of copies '
                                                                                         'available')
    stock = models.IntegerField(verbose_name='Stock', help_text='Enter the Book available', default=1)
    availability = models.BooleanField(default=True, verbose_name='Available')
    description = models.TextField(verbose_name='Description', help_text='Write something about book', null=True)
    price = models.IntegerField(verbose_name='Price', help_text='Enter the price of book', default=0)
    book_author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.book_name

    def is_available(self):
        if self.stock > 0:
            return True
        else:
            return False

    is_available.boolean = True
    is_available.short_description = 'Available'


class Member(models.Model):
    member_ID = models.AutoField(primary_key=True, verbose_name='ID')
    member_name = models.CharField(verbose_name='Name', help_text='Enter member name', max_length=100)
    member_contact_number = models.IntegerField(verbose_name='Phone number', help_text='Enter member phone number')
    member_email = models.EmailField(verbose_name='Email', help_text='Enter member Email')
    member_address = models.TextField(verbose_name='Address', help_text='Enter member address', null=True)

    def __str__(self):
        return self.member_name


class Record(models.Model):
    borrowed_ID = models.AutoField(primary_key=True, verbose_name='Order ID')
    borrowed_member = models.ForeignKey(Member, on_delete=models.CASCADE, verbose_name='Member name',
                                        help_text='Select Member name')
    borrowed_book = models.ForeignKey(Book, on_delete=models.CASCADE, verbose_name='Book name',
                                      help_text='Select Book name')
    issued_librarian = models.ForeignKey(Librarian, on_delete=models.CASCADE, verbose_name='Issued Librarian',
                                         help_text='Select librarian')
    issue_date = models.DateField(verbose_name='Issued Date', auto_now_add=True)
    return_date = models.DateField(default=date.today() + timedelta(days=7), verbose_name='Return date',
                                   help_text='Enter return date')
    is_return = models.BooleanField(default=False, help_text='Select if book is returning', verbose_name='Return')
    returned_date = models.DateField(verbose_name='Returned date', help_text='Enter if book returned',
                                     default=date.today() + timedelta(days=7))
    penalty = models.IntegerField(default=0, verbose_name='Penalty', help_text='Enter in rupee')

    def is_due(self):
        if date.today() > self.return_date and not self.is_return:
            self.penalty = (date.today() - self.return_date).days * 10
        return self.penalty

    is_due.short_description = 'Penalty'

    def return_date_calculation(self):
        if self.is_return:
            return self.return_date
        else:
            return 'Not returned'

    return_date_calculation.short_description = 'Returned date'

    def __str__(self):
        return str(self.borrowed_ID)


@receiver(signals.post_save, sender=Record)
def stock_decrement(sender, instance, created, **kwargs):
    stock = instance.borrowed_book.stock
    if created:
        if not instance.is_return:
            obj = instance.borrowed_book
            stock -= 1
            obj.stock = stock
            if stock <= 0:
                obj.availability = False
            obj.save()


@receiver(signals.pre_save, sender=Record)
def stock_increment(sender, instance, **kwargs):
    stock = instance.borrowed_book.stock
    if instance.is_return:
        stock += 1
        obj = instance.borrowed_book
        obj.stock = stock
        if obj.stock > 0:
            obj.availability = True
        obj.save()
