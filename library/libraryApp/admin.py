from django.contrib import admin
from django import forms
from .models import Libraries, Librarian, Book, Author, Member, Record


class FormRecordAdmin(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(FormRecordAdmin, self).__init__(*args, **kwargs)
        if not self.instance.borrowed_ID or self.instance.is_return:
            self.fields['is_return'].disabled = True
            self.fields['returned_date'].disabled = True
            self.fields['penalty'].disabled = True

    def clean(self):
        member_fk = self.cleaned_data.get('borrowed_member')
        is_return = self.cleaned_data.get('is_return')
        book_fk = self.cleaned_data.get('borrowed_book')
        borrow_count = Record.objects.filter(borrowed_member__member_ID=member_fk.member_ID).\
            filter(is_return=False).count()
        book_issue = Record.objects.filter(borrowed_member__member_ID=member_fk.member_ID).\
            filter(borrowed_book__isbn=book_fk.isbn).filter(is_return=False).exists()
        if book_issue and not is_return:
            raise forms.ValidationError(f'Book has been taken by {member_fk.member_name}', code='book issued')
        if borrow_count > 4 and not is_return:
            raise forms.ValidationError(f'Book borrow count is exceeded!', code='invalid')
        if book_fk.stock <= 0 and not is_return:
            raise forms.ValidationError(f'{book_fk.book_name} not available', code='not available')

        return self.cleaned_data

    def save(self, commit=True):
        return super(FormRecordAdmin, self).save(commit=commit)


class RecordAdmin(admin.ModelAdmin):
    list_display = ('borrowed_ID', 'borrowed_member', 'borrowed_book', 'issued_librarian', 'issue_date', 'return_date',
                    'is_return', 'return_date_calculation', 'is_due')
    form = FormRecordAdmin


class LibrariesAdmin(admin.ModelAdmin):
    list_display = ('library_id', 'library_address','library_contact_number')


class LibrarianAdmin(admin.ModelAdmin):
    list_display = ('librarian_ID', 'librarian_name', 'librarian_contact_no', 'belong_to')


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('author_name', 'about_author',)


class BookAdmin(admin.ModelAdmin):
    list_display = ('isbn', 'book_name', 'category', 'number_of_copy', 'stock', 'is_available', 'price')


class MemberAdmin(admin.ModelAdmin):
    list_display = ('member_ID', 'member_name', 'member_contact_number', 'member_email', 'member_address')


admin.site.register(Libraries, LibrariesAdmin)
admin.site.register(Librarian, LibrarianAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Member, MemberAdmin)
admin.site.register(Record, RecordAdmin)