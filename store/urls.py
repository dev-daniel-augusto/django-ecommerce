from django.urls import path

from .views import (
                    StoreView,
                    ProductView,
                    SearchView,
                    )


urlpatterns = [
    path('', StoreView.as_view(), name='store'),
    path('category/<slug:category_slug>/', StoreView.as_view(), name='products_by_category'),
    path('category/<slug:category_slug>/<slug:product_slug>/', ProductView.as_view(), name='single_product'),
    path('search/', SearchView.as_view(), name='search'),
]
