from django.urls import path
from .views import app,allproducts,store,cart,checkout

urlpatterns = [
                path('',app,name='app'),
                path('allproducts',allproducts,name ='allproducts'),
                
                ]
