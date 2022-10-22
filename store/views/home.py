from django.shortcuts import render, redirect
from django.views.generic.base import View, HttpResponse
from store.models.product import Products, Category
from django.views.generic.edit import CreateView
from store.forms import CategoryForm, QuantitySelect


def index(request):
    if request.method == 'POST':
        products = get_category(request)
    else:
        products = Products.get_all_products()
    form = CategoryForm
    quantity = QuantitySelect
    data = {'products': products}
    detail = details(request)
    context = {'product': data, 'details': detail, 'form': form, 'quantity_selector': quantity}
    return render(request, 'index.html', context)


def details(request):
    product = request.GET.get('chosen_product', '2')
    product_detail = Products.get_products_by_id(product)
    return product_detail


def get_category(request):
    form = CategoryForm(request.POST)
    if form.is_valid():
        category_id = request.POST.get('Choose_Category', '1')
        for selection in Category.get_category_by_id(category_id):
            if selection.name == 'all':
                products = Products.get_all_products()
            else:
                products = Products.get_all_products_by_categoryid(category_id)
            return products
    else:
        products = Products.get_all_products()
        return products


