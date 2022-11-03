from .cart import Cart


def cart_total_amount(request):
    if request.user.is_authenticated:
        cart = Cart(request)
        print(cart)
        total_bill = 0
        for key, value in request.session['cart'].items():
            print(key, value)
            line_total = (float(value['price'])) * int(value['quantity'])
            total_bill += line_total
        return {'cart_total_amount': total_bill, 'line_total': line_total}
    else:
        return {'cart_total_amount': 0, 'line_total': 0}