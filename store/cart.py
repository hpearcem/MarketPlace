from django.conf import settings
from .models.product import Products
from decimal import Decimal


class Cart(object):
    """This is a base class for the shopping cart
    attributes:
        request: A request object to use in the Cart class
        session: A session object that contains cart details
        cart: the cart object from the session, or if none exists one is created
        line_total: the total of the product price times the quantity that was added to the cart
        Methods:
            add: adds the chosen product to the cart and sets it as the new item. A check is doe to see
            if the product already exists in the cart, if so the quantity is just added to the existing
            entry. Else a new entry is created.
            save: Saves the cart to the session
            get_total_price: Returns the total of all the products * quantity in the cart.
            remove: removes an item from the cart
            clear: clears the whole cart
        """
    def __init__(self, request):
        self.request = request
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart
        self.line_total = 0

    def add(self, product, quantity=1, action=None):
        product_id = product.id
        newItem = True

        if str(product.id) not in self.cart.keys():
            self.line_total = 0
            self.cart[product.id] = {
                'userid': self.request.user.id,
                'product_id': product_id,
                'name': product.name,
                'price': str(product.price),
                'quantity': quantity,
                'line_total': str(float(product.price) * int(quantity))
            }

        else:
            newItem = True
            for key, value in self.cart.items():
                if key == str(product.id):
                    value['quantity'] = str(int(value['quantity']) + int(quantity))
                    value['line_total'] = str(float(value['price']) * int(value['quantity']))
                    newItem = False
                    self.save()
                    break

            if newItem:
                self.line_total = 0
                self.cart[product.id] = {
                    'userid': self.request,
                    'product_id': product.id,
                    'name': product.name,
                    'quantity': quantity,
                    'price': str(product.price),
                    'line_total': str(float(product.price) * int(quantity))
                }

        self.save()

    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True

    def get_total_price(self):
        return sum(float(item['price']) * int(item['quantity']) for item in self.cart.values())

    def remove(self, request, product):
        product_id = str(product.id)
        print(product_id, product, type(product_id), type(product))
        if product_id in request.session['cart'].keys():
            del self.cart[product_id]
            self.save()

    def clear(self):
        self.session[settings.CART_SESSION_ID] = {}
        self.session.modified = True


