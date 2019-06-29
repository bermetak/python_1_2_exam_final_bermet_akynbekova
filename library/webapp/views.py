from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import AuthorForm, BookForm
from .models import Author, Book, Profile


class MyDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):

    def has_permission(self):
        return self.request.user.is_superuser

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_deleted = True
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class AuthorListView(ListView):
    template_name = 'author_list.html'
    model = Author
    queryset = Author.objects.active()


class AuthorDetailView(DetailView):
    template_name = 'author_detail.html'
    model = Author


class AuthorCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    template_name = 'author_create.html'
    form_class = AuthorForm
    model = Author

    def has_permission(self):
        return self.request.user.is_superuser


class AuthorUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    template_name = 'author_update.html'
    form_class = AuthorForm
    model = Author

    def has_permission(self):
        return self.request.user.is_superuser


class AuthorDeleteView(MyDeleteView):
    template_name = 'author_delete.html'
    model = Author
    success_url = reverse_lazy('webapp:author_list')


class BookListView(ListView):
    template_name = 'book_list.html'
    model = Book
    queryset = Book.objects.active()


class BookDetailView(DetailView):
    template_name = 'book_detail.html'
    model = Book


class BookCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    template_name = 'book_create.html'
    form_class = BookForm
    model = Book

    def has_permission(self):
        return self.request.user.is_superuser

class BookUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    template_name = 'book_update.html'
    form_class = BookForm
    model = Book

    def has_permission(self):
        return self.request.user.is_superuser

class BookDeleteView(MyDeleteView):
    template_name = 'book_delete.html'
    model = Book
    success_url = reverse_lazy('webapp:book_list')

class ProfileDetailView(LoginRequiredMixin, DetailView):
    model = Profile
    template_name = 'profile.html'
