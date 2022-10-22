from decimal import Decimal
from store.models.product import Products
from django.conf import settings


class Basket:

    def __init__(self, request):
        self.session = request.session

    def test(self):
        print(self.session)
