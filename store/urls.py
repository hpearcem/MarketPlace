from django.urls import path, reverse
from .views import home

app_name = 'Market'  # Adds a namespace to the app

urlpatterns = [
    path('', home.index, name='index'),
    path('/<>/', home.category_selector, name='category_list'),
    ]
