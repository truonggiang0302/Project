from django.shortcuts import render,redirect
from .models import *
# Create your views here.

def index(request):
    return render(request,'index.html')

def viewProduct(request):
    productList=Product.objects.all()
    context={'productList':productList}
    return render(request,'view_product.html',context)