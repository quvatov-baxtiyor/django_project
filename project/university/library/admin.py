from datetime import datetime

from django.contrib import admin
from import_export.admin import ImportExportActionModelAdmin
from .models import Book, User, BookRecord


# Register your models here.

# decorator
@admin.register(Book)
class BookAdmin(ImportExportActionModelAdmin):
    search_fields = ['title', 'author']
    list_display = ['title', 'author', 'count']
    list_filter = ['author']


@admin.register(User)  # decorator sifatida classga registratsiya qilish
class UserAdmin(admin.ModelAdmin):
    search_fields = ['first_name', 'last_name']
    list_display = ['first_name', 'role']
    list_filter = ['role']


def mark_book_record_as_returned(modeladmin, request, queryset):
    queryset.filter(returned_on__isnull=True).update(returned_on=datetime.today())


@admin.register(BookRecord)
class BookRecordAdmin(admin.ModelAdmin):
    list_display = ['book', 'user', 'took_on', 'is_returned_on', ]
    autocomplete_fields = ['book', 'user']
    list_select_related = ['book', 'user']
    actions = [mark_book_record_as_returned, ]

    # def get_is_returned_on(self, book_record):
    #     return 'yes' if book_record.is_returned_on else 'no'
