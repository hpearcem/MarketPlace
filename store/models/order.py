from decimal import Decimal
from django.conf import settings
from django.db import models
from store.models.product import Products


class Order(models.Model):
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='order_user')
    created = models.DateTimeField(auto_now_add=True)
    ordered = models.BooleanField(default=False)
    order_total = models.DecimalField(default=0, max_digits=10, decimal_places=2)

    class Meta:
        ordering = ('-created',)

    @staticmethod
    def get_orders_by_user_id(user_id):
        if user_id:
            return Order.objects.filter(user_id)
        else:
            return None

    def __str__(self):
        return str(self.id)


class CartItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)
    product = models.ForeignKey(Products, related_name='order_items', on_delete=models.CASCADE, default=2)
    line_total = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return str(self.order)
