from django import forms
from .models import Author, Book


class AuthorForm(forms.ModelForm):

    class Meta:
        model = Author
        fields = ['name', 'bio', 'photo', 'birth_date', 'death_date']


class BookForm(forms.ModelForm):

    class Meta:
        model = Book
        fields = ['title', 'author', 'description', 'cover', 'published', 'file']