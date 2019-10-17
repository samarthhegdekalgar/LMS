from django.test import TestCase
from .models import Author, Book, Member, Librarian, Libraries, Record
from datetime import date


class RecordTestCase(TestCase):
    def setUp(self):
        libraries_obj = Libraries.objects.create(library_address='Banglore', library_contact_number='9876543211')
        Librarian.objects.create(librarian_name='Varun', librarian_contact_no='9879879879',
                                 belong_to=libraries_obj)
        author_obj = Author.objects.create(author_name='Paul', about_author='He is from USA')
        Book.objects.create(isbn=1234567890, book_name='Python', category='Programing',
                            number_of_copy=10, stock=10, description='This is python book', price=900,
                            book_author=author_obj)
        Member.objects.create(member_name='Samarth', member_contact_number='1231231231',
                              member_email='S@gmail.com', member_address='Bangalore')

    def test_book_stock_decrement(self):
        """
        checking the functionality of stock update when book is borrowed

        :input: book stock = 10
        :operation: decrement stock value
        :output: book stock = 9

        :return: 1

        """
        member_obj = Member.objects.get(member_name='Samarth')
        book_obj = Book.objects.get(book_name='Python')
        librarian_obj = Librarian.objects.get(librarian_name='Varun')
        initial_stock = book_obj.stock
        Record.objects.create(borrowed_member=member_obj, borrowed_book=book_obj,
                              issued_librarian=librarian_obj)
        new_book_obj = Book.objects.get(book_name='Python')
        final_stock = new_book_obj.stock
        self.assertEqual(initial_stock - final_stock, 1)

    def test_book_stock_incrementing(self):
        """
        checking the functionality of stock update when book is returned

        :input: book stock = 9
        :operation: decrement stock value
        :output: book stock = 10

        :return: 1

        """
        member_obj = Member.objects.get(member_name='Samarth')
        book_obj = Book.objects.get(book_name='Python')
        librarian_obj = Librarian.objects.get(librarian_name='Varun')
        initial_stock = book_obj.stock
        Record.objects.create(borrowed_member=member_obj, borrowed_book=book_obj,
                              issued_librarian=librarian_obj, is_return=True)
        new_book_obj = Book.objects.get(book_name='Python')
        final_stock = new_book_obj.stock
        self.assertEqual(final_stock - initial_stock, 1)

    def test_penalty_update(self):
        """
        checking the functionality of penalty for returning after due date

        :input: return date
        :operation: Find the penalty amount
        :output: 5 * 10 = 50 -> penalty value is directly depends on today's date

        :return: 50
        """
        member_obj = Member.objects.get(member_name='Samarth')
        book_obj = Book.objects.get(book_name='Python')
        librarian_obj = Librarian.objects.get(librarian_name='Varun')
        record_obj = Record.objects.create(borrowed_member=member_obj, borrowed_book=book_obj,
                                           issued_librarian=librarian_obj,
                                           is_return=False,
                                           return_date=date(2019, 10, 12))
        record_obj.is_due()
        penalty = record_obj.penalty
        self.assertEqual(penalty, 50)
