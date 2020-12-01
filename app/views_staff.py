from datetime import datetime
from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.views.generic.edit import CreateView, UpdateView
from django.utils.decorators import method_decorator
from django.conf import settings
import math
from django.contrib.auth.decorators import login_required

#Category

def listCategory(request):
    categoryList = Category.objects.all()
    context = {'categoryList': categoryList}
    return render(request, 'staff/category/list.html', context)

class CategoryCreateView(CreateView):
    model=Category
    fields='__all__'
    success_url='/staff/list-category'
    template_name='staff/category/form.html'

class CategoryUpdateView(UpdateView):
    model=Category
    fields='__all__'
    success_url='/staff/list-category'
    template_name='staff/category/form.html'

def deleteCategory(request,pk):
    c=Category.objects.get(pk=pk)
    c.delete()
    return redirect('list-category')

#Product

def listProduct(request):
    productList=Product.objects.all()
    context={'productList':productList}
    return render(request,'staff/product/list.html',context)

class ProductCreateView(CreateView):
    model=Product
    fields='__all__'
    success_url='/staff/list-product'
    template_name='staff/product/form.html'

class ProductUpdateView(UpdateView):
    model=Product
    fields='__all__'
    success_url='/staff/list-product'
    template_name='staff/product/form.html'

def deleteProduct(request,pk):
    c=Product.objects.get(pk=pk)
    c.delete()
    return redirect('list-product')

#Order
def listOrder(request):
    orderList=Order.objects.all()
    orderList=orderList.order_by('status','-order_date')
    context={
        'orderList':orderList
    }
    return render(request,'staff/order/list.html',context)

def viewOrder(request,pk):
    order=Order.objects.get(pk=pk)
    context={'order':order}
    return render(request,'staff/order/detail.html',context)

def confirmOrderDeliver(request,pk):
    order=Order.objects.get(pk=pk)
    order.status=Order.Status.DELIVERD
    order.deliver_date=datetime.now()
    order.save()
    return redirect('list-order')

def cancelOrder(request,pk):
    order=Order.objects.get(pk=pk)
    order.status=Order.Status.CANCELED
    order.save()
    return redirect('list-order')