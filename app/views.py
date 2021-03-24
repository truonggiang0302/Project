from django.shortcuts import render, redirect
from .models import *
from django.conf import settings
import math
from .forms import *
from datetime import datetime
from django.contrib.auth.decorators import login_required


# Create your views here.
PAGE_SIZE = 5
# Trang chủ
def index(request):
    return render(request, 'index.html')


@login_required
def index1(request):
    return render(request, 'index1.html')


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
    {'id': 3, 'name': '600cc --> 1000cc', 'min': 600, 'max': 1000},
    {'id': 4, 'name': 'Trên 1000cc', 'min': 1000},
]


# Tìm kiếm
def searchProduct(request):
    name = request.GET.get('name', '')
    productList = Product.objects.filter(name__icontains=name)
    page = request.GET.get('page', '')
    page = int(page) if page.isdigit() else 1
    pageSize = settings.PAGE_SIZE
    start = (page - 1) * pageSize
    end = start + pageSize
    total = productList.count()
    num_page = math.ceil(total / pageSize)
    context = {
        'productList': productList[start:end],
        'name': name,
        'start': start,
        'end': end,
        'num_page': num_page,
        'page': page,
    }
    return render(request, 'search.html', context)


# Giới thiệu
def Introduce(request):
    return render(request, 'introduce.html')


# Xem sản phẩm
def ViewAllProduct(request):
    page = request.GET.get('page', '')
    page = int(page) if page.isdigit() else 1
    pageSize = settings.PAGE_SIZE
    start = (page - 1) * pageSize
    end = start + pageSize
    productList = Product.objects.all()
    productId = request.GET.get('productId', '')
    if productId:
        productId = int(productId)
        productList = productList.filter(product__id=productId)
    categoryId = request.GET.get('categoryId', '')
    if categoryId:
        categoryId = int(categoryId)
        productList = productList.filter(category__id=categoryId)
    categoryList = Category.objects.all()
    priceId = request.GET.get('priceId')
    priceId = int(priceId) if priceId else None
    price = priceList[priceId - 1] if priceId else {}
    minPrice, maxPrice = price.get('min'), price.get('max')
    if minPrice:
        productList = productList.filter(price__gte=minPrice)

    if maxPrice:
        productList = productList.filter(price__lte=maxPrice)

    ccId = request.GET.get('ccId')
    ccId = int(ccId) if ccId else None
    cc = ccList[ccId - 1] if ccId else {}
    minCC = cc.get('min')
    maxCC = cc.get('max')
    if minCC:
        productList = productList.filter(cc__gte=minCC)
    if maxCC:
        productList = productList.filter(cc__lte=maxCC)
    total = productList.count()
    num_page = math.ceil(total / pageSize)
    # Context
    context = {
        'productList': productList[start:end],
        'start': start,
        'end': end,
        'num_page': num_page,
        'page': page,
        'priceList': priceList,
        'ccList': ccList,
        'categoryList': categoryList,
        'categoryId': categoryId,
        'priceId': priceId,
        'ccId': ccId,
        'productId': productId,
    }
    return render(request, 'view_all_product.html', context)


# Xem chi tiết sản phẩm
def viewProductDetail(request, pk):
    product = Product.objects.get(pk=pk)
    context = {'product': product}
    return render(request, 'view_detail_product.html', context)


# Mua sản phẩm
@login_required
def orderProduct(request, pk):
    product = Product.objects.get(pk=pk)
    form = OrderForm(initial={'productId':pk})
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
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


# Cảm ơn
def ThankYou(request):
    return render(request, 'thank_you.html')


# Liên hệ
@login_required
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
            contact.customer_content = data['customer_content']
            contact.contact_date = datetime.now()
            contact.save()
            return redirect('/thank-you1')
    context = {'form': form}
    return render(request, 'contact.html', context)


# thankyou1
def ThankYou1(request):
    return render(request, 'thank_you1.html')


# tin tức
def NewsView(request):
    page = request.GET.get('page', '')
    page = int(page) if page.isdigit() else 1
    start = (page - 1) * PAGE_SIZE
    end = start + PAGE_SIZE
    newsList = News.objects.all()
    total = newsList.count()
    num_page = math.ceil(total / PAGE_SIZE)
    context = {
        'newList': newsList[start:end],
        'start': start,
        'end': end,
        'num_page': num_page,
        'page': page
    }
    return render(request, 'news.html', context)


# Xem chi tiết tin tức
def NewsDetailView(request, pk):
    newsList = News.objects.get(pk=pk)
    context = {
        'newsList': newsList
    }
    return render(request, 'news_detail.html', context)
