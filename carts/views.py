from django.views.generic import TemplateView
from django.shortcuts import redirect
from store.models import Product
from carts.models import Cart, CartItem


def _get_cart_id(request):
    cart_id = request.session.session_key
    if not cart_id:
        cart_id = request.session.create()
    return cart_id


def add_product_to_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    try:
        cart = Cart.objects.get(cart_id=_get_cart_id(request))
    except Cart.DoesNotExist:
        cart = Cart.objects.create(cart_id=_get_cart_id(request))
    cart.save()
    try:
        cart_item = CartItem.objects.get(product=product,
                                         cart=cart,
                                         )
        cart_item.quantity = cart_item.quantity + 1
    except CartItem.DoesNotExist:
        cart_item = CartItem.objects.create(
            product=product,
            cart=cart,
            quantity=1,
        )
    cart_item.save()
    return redirect('cart')


def decrease_product_quantity(request, product_id):
    cart = Cart.objects.get(cart_id=_get_cart_id(request))
    product = Product.objects.get(id=product_id)
    cart_item = CartItem.objects.get(cart=cart, product=product)
    if cart_item.quantity > 1:
        cart_item.quantity = cart_item.quantity - 1
        cart_item.save()
    else:
        cart_item.delete()
    return redirect('cart')


def remove_product(request, product_id):
    cart = Cart.objects.get(cart_id=_get_cart_id(request))
    product = Product.objects.get(id=product_id)
    cart_item = CartItem.objects.get(cart=cart, product=product)
    cart_item.delete()
    return redirect('cart')


class CartView(TemplateView):
    template_name = 'cart.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        quantity = 0
        total = 0
        try:
            cart = Cart.objects.get(cart_id=_get_cart_id(self.request))
            cart_items = CartItem.objects.filter(cart=cart)
            context['cart_items'] = cart_items
            for cart_item in cart_items:
                quantity += cart_item.quantity
                total += (cart_item.quantity * cart_item.product.price)
            tax = (5 * total)/100
            final_price = f'{total + tax:.2f}'
            context['quantity'] = quantity
            context['total'] = total
            context['tax'] = tax
            context['final_price'] = final_price
        except CartItem.DoesNotExist:
            pass
        return context
