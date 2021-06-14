from django.urls import path
from .views import (
                    StoreView,
                    ProductView,
                    )

urlpatterns = [
    path('', StoreView.as_view(), name='store'),
    path('<slug:category_slug>/', StoreView.as_view(), name='products_by_category'),
    path('<slug:category_slug>/<slug:product_slug>/', ProductView.as_view(), name='single_product'),
]
