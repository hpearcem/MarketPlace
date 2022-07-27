from django.shortcuts import render, redirect, HttpResponseRedirect
from django.views import View
from store.models.product import Products
from store.models.category import Category
# from django.views.decoretors.http import require_POST, require_GET, login_reuired


class Index(View):
    # @require_POST
    def post(self, request):
        post = request.POST.get('product')
        remove = request.POST.get('remove')
        cart = request.session.get('cart')
        return redirect('home')

    # @require_GET
    def get(self, request):
        return HttpResponseRedirect(f'/store{request.get_full_path()[1:]}')


def store(request):
    """The function assigns the cart, and if there is no cart it opens an empty
    dictionary. If a category is chosen it will return all the products in the
    category else just all the products"""
    cart = request.session.get('cart')
    if not cart:
        request.session['cart'] = {}
    products = None
    categories = Category.get_all_categories()
    categoryID = request.GET.get('category')
    if categoryID:
        products = Products.get_all_products_by_categoryid(categoryID)
    else:
        products = Products.get_all_products()

    data = {}
    data['products'] = products
    data['categories'] = categories

    print('you are : ', request.session.get('email'))
    return render(request, 'index.html', data)



