from django.urls import path, reverse
from .views.home import IndexView

app_name = 'Market'  # Adds a namespace to the app

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
]
