from django.shortcuts import render, redirect
from store.models.product import Products, Category
from store.forms import CategoryForm, QuantitySelect
from .orders import cart_add


def index(request):

    if request.method == 'POST':
        products = get_category(request)
    else:
        products = Products.get_all_products()
    form = CategoryForm
    quantity_selector = QuantitySelect
    data = {'products': products}
    detail, product = details(request)
    context = {'product': data, 'details': detail, 'form': form, 'quantity_selector': quantity_selector}
    return render(request, 'index.html', context)


def details(request):
    product = request.GET.get('chosen_product', '2')
    product_detail = Products.get_products_by_id(product)
    return product_detail, product


def get_category(request):
    if 'quantity' in request.POST:
        quantity = request.POST.get('quantity', '0')
        detail, product = details(request)
        cart_add(request, product, quantity)
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


