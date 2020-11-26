from django.shortcuts import render, redirect
from .models import *
from django.conf import settings
import math
from .forms import *
from datetime import datetime
# Create your views here.

#Trang chủ
def index(request):
    return render(request,'index.html')

priceList = [
    {'id': 1, 'name': 'Dưới 100 triệu', 'max': 100},
    {'id': 2, 'name': '100 triệu --> 300 triệu', 'min': 100, 'max': 300},
    {'id': 3, 'name': '300 triệu --> 600 triệu', 'min': 300, 'max': 600},
    {'id': 4, 'name': '600 triệu --> 900 triệu', 'min': 600, 'max': 900},
    {'id': 5, 'name': 'Trên 900 triệu', 'min': 900},
]
ccList = [
    {'id': 1, 'name': 'Dưới 300cc', 'max': 300},
    {'id': 2, 'name': '300cc --> 600cc', 'min': 300, 'max': 600},
    {'id': 3, 'name': 'Trên 1000cc', 'min': 1000},
]
#Tìm kiếm
def searchProduct(request):
    name=request.GET.get('name','')
    productList=Product.objects.filter(name__icontains=name)
    context={
        'productList':productList,
        'name':name}
    return render(request,'search.html',context)

#Giới thiệu
def Introduce(request):
    return render(request,'introduce.html')

#Xem sản phẩm
def viewAllProduct(request):
    productList = Product.objects.all()
    page = request.GET.get('page', '')
    page = int(page) if page.isdigit() else 1
    pageSize = settings.PAGE_SIZE
    start = (page-1)*pageSize
    end = start + pageSize
    total = len(productList)
    num_page = math.ceil(total/pageSize)
    categoryId = request.GET.get('categoryId')
    categoryId = int(categoryId) if categoryId else None
    if categoryId:
        productList = productList.filter(category__id=categoryId)
    categoryList = Category.objects.all()
    priceId = request.GET.get('priceId')
    priceId = int(priceId) if priceId else None
    price = priceList[priceId-1] if priceId else {}
    minPrice, maxPrice = price.get('min'), price.get('max')
    if minPrice:
        productList = productList.filter(price__gte=minPrice)

    if maxPrice:
        productList = productList.filter(price__lte=maxPrice)

    ccId = request.GET.get('ccId')
    ccId = int(ccId) if ccId else None
    cc = ccList[ccId-1] if ccId else {}
    minCC = cc.get('min')
    maxCC = cc.get('max')
    if minCC:
        productList = productList.filter(cc__gte=minCC)
    if maxCC:
        productList = productList.filter(cc__lte=maxCC)
    #Context
    context = {
        'productList': productList[start:end],
        'start': start,
        'end': end,
        'num_page': num_page,
        'page': page,
        'priceList': priceList,
        'ccList':ccList,
        'categoryList': categoryList,
        'productList': productList,
        'categoryId': categoryId,
        'priceId': priceId,
        'ccId':ccId,
    }
    return render(request, 'view_all_product.html', context)

def Honda(request):
    product = Product.objects.filter(category__id=1)
    page = request.GET.get('page', '')
    page = int(page) if page.isdigit() else 1
    pageSize = settings.PAGE_SIZE
    start = (page-1)*pageSize
    end = start + pageSize
    total = len(product)
    num_page = math.ceil(total/pageSize)
    context = {
        'product': product[start:end],
        'start': start,
        'end': end,
        'total': total,
        'num_page': num_page,
        'page': page
    }
    return render(request, 'motor/honda.html', context)


def Yamaha(request):
    product = Product.objects.filter(category__id=2)
    page = request.GET.get('page', '')
    page = int(page) if page.isdigit() else 1
    pageSize = settings.PAGE_SIZE
    start = (page-1)*pageSize
    end = start + pageSize
    total = len(product)
    num_page = math.ceil(total/pageSize)
    context = {
        'product': product[start:end],
        'start': start,
        'end': end,
        'total': total,
        'num_page': num_page,
        'page': page
    }
    return render(request, 'motor/yamaha.html', context)


def Ducati(request):
    product = Product.objects.filter(category__id=3)
    page = request.GET.get('page', '')
    page = int(page) if page.isdigit() else 1
    pageSize = settings.PAGE_SIZE
    start = (page-1)*pageSize
    end = start + pageSize
    total = len(product)
    num_page = math.ceil(total/pageSize)
    context = {
        'product': product[start:end],
        'start': start,
        'end': end,
        'total': total,
        'num_page': num_page,
        'page': page
    }
    return render(request, 'motor/ducati.html', context)


def Kawasaki(request):
    product = Product.objects.filter(category__id=4)
    page = request.GET.get('page', '')
    page = int(page) if page.isdigit() else 1
    pageSize = settings.PAGE_SIZE
    start = (page-1)*pageSize
    end = start + pageSize
    total = len(product)
    num_page = math.ceil(total/pageSize)
    context = {
        'product': product[start:end],
        'start': start,
        'end': end,
        'total': total,
        'num_page': num_page,
        'page': page
    }
    return render(request, 'motor/kawasaki.html', context)


def BMW(request):
    product = Product.objects.filter(category__id=5)
    page = request.GET.get('page', '')
    page = int(page) if page.isdigit() else 1
    pageSize = settings.PAGE_SIZE
    start = (page-1)*pageSize
    end = start + pageSize
    total = len(product)
    num_page = math.ceil(total/pageSize)
    context = {
        'product': product[start:end],
        'start': start,
        'end': end,
        'total': total,
        'num_page': num_page,
        'page': page
    }
    return render(request, 'motor/bmw.html', context)


def Suzuki(request):
    product = Product.objects.filter(category__id=6)
    page = request.GET.get('page', '')
    page = int(page) if page.isdigit() else 1
    pageSize = settings.PAGE_SIZE
    start = (page-1)*pageSize
    end = start + pageSize
    total = len(product)
    num_page = math.ceil(total/pageSize)
    context = {
        'product': product[start:end],
        'start': start,
        'end': end,
        'total': total,
        'num_page': num_page,
        'page': page
    }
    return render(request, 'motor/suzuki.html', context)


def KTM(request):
    product = Product.objects.filter(category__id=7)
    page = request.GET.get('page', '')
    page = int(page) if page.isdigit() else 1
    pageSize = settings.PAGE_SIZE
    start = (page-1)*pageSize
    end = start + pageSize
    total = len(product)
    num_page = math.ceil(total/pageSize)
    context = {
        'product': product[start:end],
        'start': start,
        'end': end,
        'total': total,
        'num_page': num_page,
        'page': page
    }
    return render(request, 'motor/ktm.html', context)

#Xem chi tiết sản phẩm
def viewProductDetail(request, pk):
    product = Product.objects.get(pk=pk)
    context = {'product': product}
    return render(request, 'view_detail_product.html', context)

#Mua sản phẩm
def orderProduct(request, pk):
    product = Product.objects.get(pk=pk)
    form = OrderForm(initial={'qty': 1})
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            print('data', data)
            order = Order()
            order.product = product
            order.qty = data['qty']
            order.customer_name = data['customer_name']
            order.customer_phone = data['customer_phone']
            order.customer_address = data['customer_address']
            order.order_date = datetime.now()
            order.status = Order.Status.NEW
            order.save()
            return redirect('/thank-you')
    context = {'form': form, 'product': product}
    return render(request, 'order.html', context)

#Cảm ơn
def ThankYou(request):
    return render(request,'thank_you.html')
