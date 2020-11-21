from django.shortcuts import render, redirect
from .models import *
from django.conf import settings
import math
from .forms import *
from datetime import datetime
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

def Honda(request):
    product=Product.objects.filter(category__id=1)
    context={'product':product}
    return render(request,'motor/honda.html')

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


def orderProduct(request, pk):
    product = Product.objects.get(pk=pk)
    form = OrderForm(initial={'qty': 1})
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            print('data', data)
            order=Order()
            order.product=product
            order.qty=data['qty']
            order.customer_name=data['customer_name']
            order.customer_phone=data['customer_phone']
            order.customer_address=data['customer_address']
            order.order_date=datetime.now()
            order.status=Order.Status.NEW
            order.save()
            return redirect('/thank-you')
    context = {'form': form, 'product': product}
    return render(request, 'order.html', context)
