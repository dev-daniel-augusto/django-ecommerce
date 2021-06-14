from rest_framework import serializers
from store.models import Product


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = (
                'id',
                'product_name',
                'product_description',
                'is_available',
                'category',
                'price',
                'image',
                'stock',
                'slug',
                 )
