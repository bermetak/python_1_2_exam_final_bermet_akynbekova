from django.contrib import admin
from .models import Author


class AuthorAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name']


admin.site.register(Author, AuthorAdmin)