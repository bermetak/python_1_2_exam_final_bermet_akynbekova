from django import forms
from .models import Author


class AuthorForm(forms.ModelForm):

    class Meta:
        model = Author
        fields = ['name', 'bio', 'photo', 'birth_date', 'death_date']