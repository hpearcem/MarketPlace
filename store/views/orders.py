from django.shortcuts import render, redirect
from store.models.product import Products
from django.contrib.auth.decorators import login_required
from store.cart import Cart


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
    # print(request.session['cart'].keys())
    cart = Cart(request)
    return render(request, 'cart_detail.html', {'cart': cart})


