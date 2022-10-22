from django.urls import path, reverse
from .views import home, orders, auth


app_name = 'Market'  # Adds a namespace to the app

urlpatterns = [
    path('', home.index, name='index'),
    path('basket/', orders.view_basket, name='basket'),
    path("registration/signup/", auth.SignUpView.as_view(), name="signup"),
    ]
