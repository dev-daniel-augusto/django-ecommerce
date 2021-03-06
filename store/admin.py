from django.contrib import admin
from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('product_name',)}
    list_display = (
        'product_name',
        'category',
        'stock',
        'price',
        'slug',
        'is_available',
    )
