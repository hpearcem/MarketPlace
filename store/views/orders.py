from django.shortcuts import render, redirect, reverse
from store.models.product import Products
from store.models.order import Order, CartItem
from django.contrib.auth.decorators import login_required
from store.cart import Cart
from django.http import HttpResponse
from store.forms import OrderCreateForm


@login_required(login_url='login')
def cart_add(request, product, quantity):
    """This function is only available when the user is logged in, it pulls the cart and adds the selected product
    and quantity to the cart, returning a redirect to the home page"""
    cart = Cart(request)
    product = Products.get_products_by_id(product)
    cart.add(product=product, quantity=quantity)
    return redirect('/')


@login_required(login_url='login')
def cart_clear(request):
    """This function is only available when the user is logged in, the content of the cart is cleared using
    the clear() method from the cart class"""
    cart = Cart(request)
    cart.clear()
    return redirect('cart_detail.html', {'cart': cart})


@login_required(login_url='login')
def cart_detail(request):
    """This function is only available when the user is logged in, renders all the items added to the cart
    in the cart_detail.html page"""
    cart = Cart(request)
    return render(request, 'cart_detail.html', {'cart': cart})


@login_required(login_url='login')
def invoice(request):
    """This function is only available when the user is logged in, creates an invoice of the cart items,
    and clears the cart after creation. CartItems are created in the database for all items in the cart
    attributes:
        call: a call to the cart
        cart: the full cart
        cart_total: the total price of all the items in the cart obtained via the get_total_price() method
        order_id: captures the order id after the order has been created in the database
        order_date: pulls the date information from the created column in the order database
        user: the user placing the order
        order: saves the order to the database
        product: gets the products in the order from the database
        invoice_items: a library of all the items from the order database to populate the invoice
        """
    call = Cart(request)
    cart = call.session.get('cart')
    cart_total = Cart.get_total_price(call)
    order_id = ''
    order_date = ''
    if 'invoice' in request.POST:
        user = request.user
        order = Order.objects.create(user_id=user, ordered=True, order_total=cart_total)
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
    """Returns the items for the invoice from the database"""
    items = CartItem.objects.filter(order=order)
    return items
