from django.db import models

# Create your models here.
from django.urls import reverse


class SoftDeleteManager(models.Manager):
    def active(self):
        return self.filter(is_deleted=False)

    def deleted(self):
        return self.filter(is_deleted=True)


class Author(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False)
    birth_date = models.DateField(blank=True, null=True)
    death_date = models.DateField(blank=True, null=True)
    bio = models.TextField(max_length=5000, blank=True, null=True)
    photo = models.ImageField(upload_to='photos', blank=True, null=True)
    is_deleted = models.BooleanField(default=False)

    objects = SoftDeleteManager()

    def __str__(self):
        return f"{self.pk}, {self.name}"

    def get_absolute_url(self):
        return reverse('webapp:author_detail', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = "Автор"
        verbose_name_plural = "Авторы"



class Book(models.Model):
    title = models.CharField(max_length=255, blank=False, null=False)
    author = models.ForeignKey(Author, blank=False, null=False, on_delete=models.CASCADE, related_name='books')
    published = models.CharField(max_length=4, null=False, blank=False)
    file = models.FileField(upload_to='books', blank=True, null=True)
    cover = models.ImageField(upload_to='covers', blank=True, null=True)
    description = models.TextField(max_length=5000, blank=True, null=True)
    is_deleted = models.BooleanField(default=False)

    objects = SoftDeleteManager()

    def __str__(self):
        return f"{self.pk}, {self.title}"

    def get_absolute_url(self):
        return reverse('webapp:book_detail', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"