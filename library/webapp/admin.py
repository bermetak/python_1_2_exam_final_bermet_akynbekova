from django.contrib import admin
from .models import Author, Book, Profile
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin


class AuthorAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name']

class BookAdmin(admin.ModelAdmin):
    list_display = ['pk', 'title']

class ProfileInline(admin.StackedInline):
    model = Profile

class ProfileAdmin(UserAdmin):
    inlines = [ProfileInline]


admin.site.unregister(User)
admin.site.register(User, ProfileAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)