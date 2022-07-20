from django.contrib import admin
from django.urls import path
from .views import home

app_name = 'Market'  # Adds a namespace to the app

urlpatterns = [
    path('', home.post, name='home'),
    ]

