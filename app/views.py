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
    page = request.GET.get('page', '')
    page = int(page) if page.isdigit() else 1
    pageSize = settings.PAGE_SIZE
    start = (page-1)*pageSize
    end = start + pageSize
    total = productList.count()
    num_page = math.ceil(total/pageSize)
    context={
        'productList':productList[start:end],
        'name':name,
        'start': start,
        'end': end,
        'num_page': num_page,
        'page': page,
        }
    return render(request,'search.html',context)

#Giới thiệu
def Introduce(request):
    return render(request,'introduce.html')

#Xem sản phẩm
def ViewAllProduct(request):
    page = request.GET.get('page', '')
    page = int(page) if page.isdigit() else 1
    pageSize = settings.PAGE_SIZE
    start = (page-1)*pageSize
    end = start + pageSize
    productList = Product.objects.all()
    categoryId = request.GET.get('categoryId','')
    if categoryId:
        categoryId = int(categoryId)
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
    total = productList.count()
    num_page = math.ceil(total/pageSize)
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
        'categoryId': categoryId,
        'priceId': priceId,
        'ccId':ccId,
    }
    return render(request, 'view_all_product.html', context)

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

#Liên hệ
def ContactView(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            print('data', data)
            contact = Contact()
            contact.customer_name = data['customer_name']
            contact.customer_email = data['customer_email']
            contact.customer_phone = data['customer_phone']
            contact.customer_content=data['customer_content']
            contact.order_date = datetime.now()
            contact.save()
            return redirect('/thank-you')
    context = {'form': form}
    return render(request, 'contact.html', context)