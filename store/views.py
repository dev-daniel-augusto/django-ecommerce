from django.views.generic import TemplateView
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404
from django.db.models import Q

from category.models import Category
from carts.models import CartItem
from .models import Product
from carts.views import _get_cart_id


class StoreView(TemplateView):
    template_name = 'store.html'

    def get_context_data(self, category_slug=None, **kwargs):
        context = super().get_context_data(**kwargs)
        category = None
        products = None
        if category_slug is not None:
            category = get_object_or_404(Category, slug=category_slug)
            products = Product.objects.all().filter(category=category)
            paginator = Paginator(products, 9)
            page = self.request.GET.get('page')
            paged_products = paginator.get_page(page)
            context['products'] = paged_products
            context['products_count'] = products.count()
            return context
        else:
            products = Product.objects.all().filter(is_available=True)
            products_count = products.count()
            paginator = Paginator(products, 9)
            page = self.request.GET.get('page')
            paged_products = paginator.get_page(page)
            context['products_count'] = products_count
            context['categories'] = Category.objects.all()
            context['products'] = paged_products
            return context


class ProductView(TemplateView):
    template_name = 'product_detail.html'

    def get_context_data(self, category_slug=None, product_slug=None, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            product = Product.objects.get(category__slug=category_slug, slug=product_slug)
            in_cart = CartItem.objects.filter(cart__cart_id=_get_cart_id(self.request), product=product).exists()
            context['product'] = product
            context['added'] = in_cart
        except Exception as error:
            raise error
        return context


class SearchView(TemplateView):
    template_name = 'store.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if 'keyword' in self.request.GET:
            keyword = self.request.GET['keyword']
            if keyword:
                products = Product.objects.filter(
                    Q(product_description__icontains=keyword) |
                    Q(product_name__icontains=keyword)
                )
                context['products'] = products
                context['keyword'] = keyword
                return context
