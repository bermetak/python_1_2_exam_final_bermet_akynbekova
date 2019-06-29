from django.contrib import admin
from .models import Author, Book


class AuthorAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name']

class BookAdmin(admin.ModelAdmin):
    list_display = ['pk', 'title']


admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)