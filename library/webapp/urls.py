from django.urls import path
from .views import AuthorListView, AuthorDetailView, AuthorCreateView, AuthorUpdateView, AuthorDeleteView, \
    BookListView, BookDetailView, BookCreateView, BookUpdateView, BookDeleteView, ProfileDetailView

app_name = 'webapp'

urlpatterns = [
    path('authors/', AuthorListView.as_view(), name='author_list'),
    path('authors/<int:pk>/', AuthorDetailView.as_view(), name='author_detail'),
    path('authors/create/', AuthorCreateView.as_view(), name='author_create'),
    path('authors/<int:pk>/edit/', AuthorUpdateView.as_view(), name='author_update'),
    path('authors/<int:pk>/delete/', AuthorDeleteView.as_view(), name='author_delete'),
    path('', BookListView.as_view(), name='book_list'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book_detail'),
    path('books/create/', BookCreateView.as_view(), name='book_create'),
    path('books/<int:pk>/edit/', BookUpdateView.as_view(), name='book_update'),
    path('books/<int:pk>/delete/', BookDeleteView.as_view(), name='book_delete'),
    path('profile/<int:pk>/', ProfileDetailView.as_view(), name='profile_detail'),


]