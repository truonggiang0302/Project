from django.shortcuts import render, redirect
from .models import *
# Create your views here.


def index(request):
    return render(request, 'index.html')


def viewAllProduct(request):
    productList=Product.objects.all()
    context = {'productList': productList}
    return render(request, 'view_all_product.html', context)

def viewProduct(request):
    productList = Product.objects.filter(category__id=1)
    context={
        'productList':productList
    }
    return render(request,'view_product',context)