from carts.models import Cart, CartItem
from carts.views import _get_cart_id


def counter(request):
    total = 0
    try:
        cart = Cart.objects.filter(cart_id=_get_cart_id(request))
        cart_items = CartItem.objects.all().filter(cart=cart[:1])
        for cart_item in cart_items:
            total = total + cart_item.quantity
    except Cart.DoesNotExist:
        total = 0
    return dict(cart_counter=total)
