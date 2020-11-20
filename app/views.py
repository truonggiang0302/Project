from django.shortcuts import render, redirect
from .models import *
from django.conf import settings
import math
# Create your views here.


def index(request):
    return render(request, 'index.html')


def viewAllProduct(request):
    productList = Product.objects.all()
    page = request.GET.get('page', '')
    page = int(page) if page.isdigit() else 1
    pageSize = settings.PAGE_SIZE
    start = (page-1)*pageSize
    end = start + pageSize
    total = len(productList)
    num_page = math.ceil(total/pageSize)
    context = {
        'productList': productList[start:end],
        'start': start,
        'end': end,
        'total': total,
        'num_page': num_page,
        'page': page
        }
    return render(request, 'view_all_product.html', context)


def viewProduct(request, pk):
    productList = Product.objects.filter(category__id=pk)
    page = request.GET.get('page', '')
    page = int(page) if page.isdigit() else 1
    pageSize = settings.PAGE_SIZE
    start = (page-1)*pageSize
    end = start + pageSize
    total = len(productList)
    num_page = math.ceil(total/pageSize)
    context = {
        'productList': productList[start:end],
        'start': start,
        'end': end,
        'total': total,
        'num_page': num_page,
        'page': page
        }
    return render(request, 'view_product.html', context)


def viewProductDetail(request, pk):
    product = Product.objects.get(pk=pk)
    context = {'product': product}
    return render(request, 'view_detail_product.html', context)
