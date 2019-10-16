from django.contrib import admin
from django import forms
from .models import Libraries, Librarian, Book, Author, Member, Record


class FormRecordAdmin(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(FormRecordAdmin, self).__init__(*args, **kwargs)
        if not self.instance.borrowed_ID:
            self.fields['is_return'].disabled = True
            self.fields['returned_date'].disabled = True

    def clean(self):
        member_id = self.cleaned_data.get('borrowed_member')
        borrow_count = Record.objects.filter(borrowed_member__member_ID=member_id.member_ID).filter(is_return=False).count()
        if borrow_count > 4:
            raise forms.ValidationError(f'Book borrow count is exceeded!', code='invalid')
        return self.cleaned_data

    def save(self, commit=True):
        return super(FormRecordAdmin, self).save(commit=commit)


class RecordAdmin(admin.ModelAdmin):
    form = FormRecordAdmin


admin.site.register(Libraries)
admin.site.register(Librarian)
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Member)
admin.site.register(Record, RecordAdmin)