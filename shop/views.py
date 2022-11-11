from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Product

def allproducts(request):
        template = loader.get_template('shop/allproducts.html')
        context = {'allproducts': Product.objects.all()}
        return HttpResponse(template.render(context, request))
# Create your views here.
