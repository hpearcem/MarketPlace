from django.urls import path
from .views import home, orders, auth


app_name = 'Market'  # Adds a namespace to the app

urlpatterns = [
    path('', home.index, name='index'),
    path("registration/signup/", auth.SignUpView.as_view(), name="signup"),
    path('add/<int:id>/', orders.cart_add, name='cart_add'),
    path('cart_clear/', orders.cart_clear, name='cart_clear'),
    path('cart_detail/', orders.cart_detail, name='cart_detail'),
    path('cart_detail/invoice/', orders.invoice, name='invoice'),
    ]
