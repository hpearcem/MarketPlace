from django.shortcuts import render, redirect, reverse
from store.models.product import Products
from store.models.order import Order, CartItem
from django.contrib.auth.decorators import login_required
from store.cart import Cart
from django.http import HttpResponse
from store.forms import OrderCreateForm


@login_required(login_url='login')
def cart_add(request, product, quantity):
    cart = Cart(request)
    product = Products.get_products_by_id(product)
    cart.add(product=product, quantity=quantity)
    return redirect('/')


@login_required(login_url='login')
def item_clear(request, id):
    cart = Cart(request)
    product = Products.get_products_by_id(str(id))
    cart.remove(request, product=product)
    return redirect('/cart_detail/')


@login_required(login_url='login')
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect('cart_detail.html', {'cart': cart})


@login_required(login_url='login')
def cart_detail(request):
    cart = Cart(request)
    return render(request, 'cart_detail.html', {'cart': cart})


@login_required(login_url='login')
def invoice(request):
    call = Cart(request)
    cart = call.session.get('cart')
    cart_total = Cart.get_total_price(call)
    order_id = ''
    order_date = ''
    if 'invoice' in request.POST:
        user = request.user
        order = Order.objects.create(user_id=user, ordered=True)
        order_id = str(order)
        order_date = order.created
        for item in cart.values():
            product = Products.get_products_by_id(str(item['product_id']))
            CartItem.objects.create(order=order, product=product, price=item['price'],
                                    quantity=item['quantity'], line_total=item['line_total'])

    invoice_items = get_invoice_items(order_id)
    cart_clear(request)
    return render(request, 'invoice.html', {'invoice_items': invoice_items, 'invoice_nr': order_id,
                                            'order_date': order_date, 'cart_total': cart_total})


def get_invoice_items(order):
    items = CartItem.objects.filter(order=order)
    return items
