from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import AuthorForm
from .models import Author


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

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class AuthorUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    template_name = 'author_update.html'
    form_class = AuthorForm
    model = Author
    #
    # def get_permission_required(self):
    #     return None

    def has_permission(self):
        return self.request.user.is_superuser


class AuthorDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    template_name = 'author_delete.html'
    model = Author
    success_url = reverse_lazy('webapp:author_list')

    def has_permission(self):
        return self.request.user.is_superuser

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_deleted = True
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())
