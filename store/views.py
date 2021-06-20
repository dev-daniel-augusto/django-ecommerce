from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView
from django.db.models import Q
from category.models import Category
from carts.models import CartItem
from carts.views import _get_cart_id
from .models import Product


class StoreView(TemplateView):
    template_name = 'store.html'

    def get_context_data(self, category_slug=None, **kwargs):
        context = super().get_context_data(**kwargs)
        categories = None
        products = None
        if category_slug != None:
            categories = get_object_or_404(Category, slug=category_slug)
            context['products'] = products = Product.objects.all().filter(category=categories)
            context['products_count'] = products.count()
            return context
        else:
            context['products'] = Product.objects.all().filter(is_available=True)
            products_count = context['products'].count()
            context['products_count'] = products_count
            context['categories'] = Category.objects.all()
            return context
