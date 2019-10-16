from django.db import models
from datetime import date, timedelta


class Libraries(models.Model):
    library_id = models.AutoField(primary_key=True)
    library_address = models.TextField(verbose_name='Address', help_text='Enter library address')
    library_contact_number = models.IntegerField(verbose_name='Phone number', help_text='Enter library contact number')

    def __str__(self):
        return str(self.library_id)


class Librarian(models.Model):
    librarian_ID = models.AutoField(primary_key=True)
    librarian_name = models.CharField(verbose_name='Name', max_length=100, help_text='Enter Librarian Name')
    librarian_contact_no = models.IntegerField(verbose_name='Phone number', help_text='Enter Librarian contact number')
    belong_to = models.ForeignKey(Libraries,verbose_name='Library ID', help_text='Select library ID',
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
    availability = models.BooleanField(default=True)
    description = models.TextField(verbose_name='Description', help_text='Write something about book', null=True)
    price = models.IntegerField(verbose_name='Price', help_text='Enter the price of book', default=0)
    book_author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.book_name


class Member(models.Model):
    member_ID = models.AutoField(primary_key=True)
    member_name = models.CharField(verbose_name='Name', help_text='Enter member name', max_length=100)
    member_contact_number = models.IntegerField(verbose_name='Phone number', help_text='Enter member phone number')
    member_email = models.EmailField(verbose_name='Email', help_text='Enter member Email')
    member_address = models.TextField(verbose_name='Address', help_text='Enter member address', null=True)

    def __str__(self):
        return self.member_name


class Record(models.Model):
    borrowed_ID = models.AutoField(primary_key=True)
    borrowed_member = models.ForeignKey(Member, on_delete=models.CASCADE, verbose_name='Member name',
                                        help_text='Select Member name')
    borrowed_book = models.ForeignKey(Book, on_delete=models.CASCADE, verbose_name='Book name',
                                      help_text='Select Book name')
    issued_librarian = models.ForeignKey(Librarian, on_delete=models.CASCADE, verbose_name='Issued Librarian',
                                         help_text='Select librarian')
    book_quantity = models.IntegerField(verbose_name='Number of Book', help_text='Enter book quantity', default=1)
    issue_date = models.DateField(verbose_name='Issued Date', auto_now_add=True)
    return_date = models.DateField(default=date.today() + timedelta(days=7), verbose_name='Return date',
                                   help_text='Enter return date')
    is_return = models.BooleanField(default=False, help_text='Select if book is returning', verbose_name='Return')
    returned_date = models.DateField(verbose_name='Returned date', help_text='Enter if book returned', null=True)

    class Meta:
        unique_together = ['borrowed_member', 'borrowed_book', 'is_return']

    def is_due(self):
        pass

    def __str__(self):
        return str(self.borrowed_ID)
