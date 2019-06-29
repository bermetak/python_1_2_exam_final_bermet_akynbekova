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
    photo = models.ImageField(upload_to='uploads/photos', blank=True, null=True)
    is_deleted = models.BooleanField(default=False)

    objects = SoftDeleteManager()

    def __str__(self):
        return f"{self.pk}, {self.name}"

    def get_absolute_url(self):
        return reverse('webapp:author_detail', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = "Автор"
        verbose_name_plural = "Авторы"



