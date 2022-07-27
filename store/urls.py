from django.contrib import admin
from django.urls import path
from .views.home import Index, store

app_name = 'Market'  # Adds a namespace to the app

urlpatterns = [
    path('', Index.as_view(), name='home'),
    path('store', store , name='store'),
    ]

