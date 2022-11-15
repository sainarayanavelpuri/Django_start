from django.shortcuts import render
from django.http import HttpResponse

from django.template import loader

from .models import Product

def app(request):
    return render(request,'shop/loginn.html')

def allproducts(request):
    template = loader.get_template('shop/allproducts.html')
    context = {'allproducts': Product.objects.all()}
    return HttpResponse(template.render(context, request))
    ##products  = Product.objects.all()
    #context = {'products':products}
    #return HttpResponse(render(request,'shop/allproducts.html'))
def setsession(request):
    request.sessions["Name"]="some name"
    request.sessions["email"]="some email"
    return HttpResponse("section is set")
def getsession(request):
    studentName=request.session["Name"]
    studentEmail=request.session["email"]
    return HttpResponse(studentName+""+studentEmail)
# Create your views here.


