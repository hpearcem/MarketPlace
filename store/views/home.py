from django.shortcuts import render
from django.views.generic.base import View
from store.models.product import Products
from django.core import serializers


class IndexView(View):
    """IndexView is the view for the index.html page, this is the home page
    Variables:
        products - a queryset of all products in the database.
        data - initialize a dictionary to fill with products for display on the home page"""
    products = Products.get_all_products()
    data = {}

    def get(self, request, *args, **kwargs):
        """This handles the GET request sent from the browser and renders the index.html
        template.
         Variables:
             product_id - Gets the product id from the template when a product is clicked
             details - uses the product id from the details product and gets the product queryset from the database
             context - This is the dictionary object sent to the render the homepage"""
        product_id = request.GET.get('chosen_product', '2')
        details = Products.get_products_by_id(str(product_id))
        self.data['products'] = self.products
        context = {'product': self.data, 'details': details}
        return render(request, 'index.html', context)
