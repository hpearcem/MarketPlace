from django.shortcuts import render, redirect
from store.models.product import Products, Category
from store.forms import CategoryForm, QuantitySelect
from .orders import cart_add


def index(request):
    """The view for the creation of the home page, it looks for a POST request, if a category is selected.
    otherwise it renders all products.
    Attributes:
        form: pulls in the category selection form
        quantity_selector: pulls in the QuantitySelect form
        data: All the product date is stored in this library
        detail: the selected product detail as obtained from the details() function
        product: the chosen product obtained from the details() function
        Context: sets up the full view context to be rendered
        """
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
    """receives the GET request and uses the chosen product id to get the product details from the database
    and returns both product id and detail
    """
    product = request.GET.get('chosen_product', '2')
    product_detail = Products.get_products_by_id(product)
    return product_detail, product


def get_category(request):
    """If the POST request is for a quantity, the product is retrieved and the chosen product is added to the cart,
    else the category that was selected is used to populate the products library to pass on to the index view."""
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


