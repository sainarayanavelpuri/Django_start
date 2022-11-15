from django.urls import path
from .views import app,allproducts,store,cart,checkout

urlpatterns = [
                path('',app,name='apps'),
                path('allproducts',allproducts,name ='allproducts'),
                
                ]
