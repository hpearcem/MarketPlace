from django.shortcuts import render, redirect
from django.views.generic.base import View, HttpResponse
from store.models.product import Products, Category


def index(request):
    products = Products.get_all_products()
    data = {'products': products}
    detail = details(request)
    context = {'product': data, 'details': detail}
    return render(request, 'index.html', context)


def details(request):
    product = request.GET.get('chosen_product', '2')
    product_detail = Products.get_products_by_id(product)
    return product_detail


def category_selector(request):
    categories = Category.get_all_categories()
    category_id = request.GET.get('category', 'all')
    products = Products.get_all_products_by_categoryid(category_id)
    cat_list = {'categories': categories}
    context = {'categories': cat_list, 'product': products}
    return render(request, 'index/category.html', context)

