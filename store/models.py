from django.db import models
from django.urls import reverse
from stdimage import StdImageField
from category.models import Category
from category.models import new_filename
from user.models import Base


class Product(Base):
    product_name = models.CharField(max_length=150, unique=True)
    product_description = models.TextField(max_length=500, blank=True)
    is_available = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image = StdImageField(upload_to=new_filename)
    stock = models.IntegerField()
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def get_url(self):
        return reverse('single_product', args=[self.category.slug, self.slug])

    def __str__(self):
        return self.product_name
