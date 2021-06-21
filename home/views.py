from django.views.generic import ListView

from store.models import Product


class IndexView(ListView):
    models = Product
    queryset = Product.objects.order_by('price').all().filter(is_available=True)
    context_object_name = 'products'
    template_name = 'index.html'
