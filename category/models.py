from django.db import models
from django.urls import reverse
from stdimage import StdImageField
from uuid import uuid4


def new_filename(_instance, filename):
    ext = filename.split('.')
    return f'{uuid4()}.{ext}'


class Category(models.Model):
    category_name = models.CharField(max_length=50, unique=True)
    category_description = models.TextField(max_length=250, blank=True)
    category_image = StdImageField(upload_to=new_filename)
    slug = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def get_url(self):
        return reverse('products_by_category', args=[self.slug])

    def __str__(self):
        return self.category_name
