from django.urls import path
from .views import CartView
from . import views

urlpatterns = [
    path('', CartView.as_view(), name='cart'),
    path('add_cart/<int:product_id>/', views.add_product_to_cart, name='add_product'),
    path('decrase_quantity/<int:product_id>/', views.decrease_product_quantity, name='decrease_product'),
    path('remove_product/<int:product_id>/', views.remove_product, name='remove_product')
]
