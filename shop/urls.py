from django.urls import path, include
from .views import allproducts

urlpatterns = [
        path('', allproducts, name = 'allproducts'),
        ]
