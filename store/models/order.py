from django.conf import settings
from django.db import models
from store.models.product import Products  # Imports the product model

"""The models will crate database tables for the application. The models have been split
but can all be in one models file. Splitting the file makes scaling up easier as the application grows"""


class Order(models.Model):
    """The order table will capture the orders and will be linked to the user and to the cart items for the
    specific order.
    Columns:
        user_id: a foreign key that shows which client placed the order
         created: the time and date when an order was created
         ordered: a boolean flag to state that the order has been placed
         order_total: the total cost of the order
    Class:
        Meta: Meta data instructions
    Methods:
        __str__: returns the name as a string
        """
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='order_user')
    created = models.DateTimeField(auto_now_add=True)
    ordered = models.BooleanField(default=False)
    order_total = models.DecimalField(default=0, max_digits=10, decimal_places=2)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return str(self.id)


class CartItem(models.Model):
    """CartItem is the items that make up an order, this is linked to the order via an order ID
    Columns:
        order: Foreign key linking the item to an order
        price: The price of the product
        quantity: the quantity of the product that was ordered
        product: a foreign key linking to the ordered product
        line_total:  the total cost of the ordered quantity of the specific product
    Methods:
        __str__: returns the name as a string"""
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)
    product = models.ForeignKey(Products, related_name='order_items', on_delete=models.CASCADE, default=2)
    line_total = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return str(self.order)
