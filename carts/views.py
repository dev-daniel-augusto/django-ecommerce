from django.views.generic import TemplateView
from django.shortcuts import redirect
from store.models import Product
from carts.models import Cart, CartItem


def _get_cart_id(request):
    cart_id = request.session.session_key
    if not cart_id:
        cart_id = request.session.create()
    return cart_id
