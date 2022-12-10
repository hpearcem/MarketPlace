from .cart import Cart


def cart_total_amount(request):
    """Allows the cart class to return the carts total amount"""
    if request.user.is_authenticated:
        cart = Cart(request)
        total_bill = 0
        for key, value in request.session['cart'].items():
            line_total = (float(value['price'])) * int(value['quantity'])
            total_bill += line_total
        return {'cart_total_amount': total_bill, 'line_total': line_total}
    else:
        return {'cart_total_amount': 0, 'line_total': 0}