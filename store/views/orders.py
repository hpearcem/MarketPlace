from django.shortcuts import render, redirect
from store.models.product import Products, Category
from store.forms import CategoryForm, QuantitySelect
from .home import details
from store.basket import Basket


def view_basket(request):
    print(request)
    return render(request, 'basket.html')

