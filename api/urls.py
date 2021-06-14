from django.urls import path
from .views import ProductsAPIView, ProductAPIView

urlpatterns = [
    path('products/', ProductsAPIView.as_view(), name='products_api'),
    path('products/<int:pk>/', ProductAPIView.as_view(), name='product_api')
]
