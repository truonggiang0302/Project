from datetime import datetime
from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.views.generic.edit import CreateView, UpdateView
from django.utils.decorators import method_decorator
from django.conf import settings
import math
from django.contrib.auth.decorators import login_required
from django.db.models import Sum

PAGE_SIZE = 5

@login_required
def dashboard(request):
    total_category = Category.objects.count()
    total_product = Product.objects.count()
    total_contact = Contact.objects.count()
    total_order = Order.objects.count()
    orders = Order.objects.all().order_by('-id')
    page = request.GET.get('page', '')
    page = int(page) if page.isdigit() else 1
    start = (page - 1) * PAGE_SIZE
    end = start + PAGE_SIZE
    total = orders.count()
    num_page = math.ceil(total / PAGE_SIZE)
    total_qty=Product.objects.all().aggregate(Sum('qty'))
    total_qty_sell=Order.objects.all().aggregate(Sum('qty'))
    total_revenue=Order.objects.all().aggregate(Sum('product__price'))
    context = {
        'product': total_qty["qty__sum"],
        'category': total_category,
        'contact': total_contact,
        'order': total_order,
        'orders': orders[start:end],
        'start': start,
        'end': end,
        'num_page': num_page,
        'page': page,
        'qty_sell':total_qty_sell["qty__sum"],
        'revenue':total_revenue["product__price__sum"]
    }
    return render(request, 'staff/dashboard/dashboard.html', context)
# Category
@login_required
def listCategory(request):
    page = request.GET.get('page', '')
    page = int(page) if page.isdigit() else 1
    start = (page-1) * PAGE_SIZE
    end = start + PAGE_SIZE
    categoryList = Category.objects.all()
    total = categoryList.count()
    numpage = math.ceil(total/PAGE_SIZE)
    context = {
        'categoryList': categoryList[start:end],
        'page': page,
        'start': start,
        'end': end,
        'numpage': numpage,
    }
    return render(request, 'staff/category/list.html', context)

@method_decorator(login_required,name='dispatch')
class CategoryCreateView(CreateView):
    model = Category
    fields = '__all__'
    success_url = '/staff'
    template_name = 'staff/category/form.html'

@method_decorator(login_required,name='dispatch')
class CategoryUpdateView(UpdateView):
    model = Category
    fields = '__all__'
    success_url = '/staff'
    template_name = 'staff/category/form.html'

@login_required
def deleteCategory(request, pk):
    c = Category.objects.get(pk=pk)
    c.delete()
    return redirect('/staff')

# Product

@login_required
def listProduct(request):
    page = request.GET.get('page', '')
    page = int(page) if page.isdigit() else 1
    start = (page-1) * PAGE_SIZE
    end = start + PAGE_SIZE
    productList = Product.objects.all()
    total = productList.count()
    numpage = math.ceil(total/PAGE_SIZE)
    context = {
        'productList': productList[start:end],
        'page': page,
        'start': start,
        'end': end,
        'numpage': numpage,
    }
    return render(request, 'staff/product/list.html', context)

@method_decorator(login_required,name='dispatch')
class ProductCreateView(CreateView):
    model = Product
    fields = '__all__'
    success_url = '/staff/list-product'
    template_name = 'staff/product/form.html'

@method_decorator(login_required,name='dispatch')
class ProductUpdateView(UpdateView):
    model = Product
    fields = '__all__'
    success_url = '/staff/list-product'
    template_name = 'staff/product/form.html'

@login_required
def deleteProduct(request, pk):
    p = Product.objects.get(pk=pk)
    p.delete()
    return redirect('list-product')

# Order

@login_required
def listOrder(request):
    page = request.GET.get('page', '')
    page = int(page) if page.isdigit() else 1
    start = (page-1) * PAGE_SIZE
    end = start + PAGE_SIZE
    orderList = Order.objects.all()
    orderList = orderList.order_by('status', '-order_date')
    total = orderList.count()
    numpage = math.ceil(total/PAGE_SIZE)
    context = {
        'orderList': orderList[start:end],
        'page': page,
        'start': start,
        'end': end,
        'numpage': numpage,
    }
    return render(request, 'staff/order/list.html', context)

@login_required
def viewOrder(request, pk):
    order = Order.objects.get(pk=pk)
    context = {'order': order}
    return render(request, 'staff/order/detail.html', context)

@login_required
def confirmOrderDeliver(request, pk):
    order = Order.objects.get(pk=pk)
    order.status = Order.Status.DELIVERD
    order.deliver_date = datetime.now()
    order.save()
    return redirect('list-order')

@login_required
def confirmOrderReceive(request,pk):
    order=Order.objects.get(pk=pk)
    order.status=Order.Status.RECEIVED
    order.deliver_date=datetime.now()
    order.save()
    return redirect('list-order')
@login_required
def cancelOrder(request, pk):
    order = Order.objects.get(pk=pk)
    order.status = Order.Status.CANCELED
    order.save()
    return redirect('list-order')

@login_required
def deleteOrder(request,pk):
    order=Order.objects.get(pk=pk)
    order.delete()
    return redirect('list-order')
# CONTACT
@login_required
def listContact(request):
    page = request.GET.get('page', '')
    page = int(page) if page.isdigit() else 1
    pageSize=settings.PAGE_SIZE
    start = (page-1) * pageSize
    end = start + pageSize
    contactList = Contact.objects.all()
    contactList = contactList.order_by('-contact_date')
    total = contactList.count()
    numpage = math.ceil(total/pageSize)
    context = {
        'contactList': contactList[start:end],
        'page': page,
        'start': start,
        'end': end,
        'numpage': numpage,
    }
    return render(request, 'staff/contact/list.html', context)

@login_required
def viewContact(request,pk):
    contact=Contact.objects.get(pk=pk)
    context={
        'contact':contact
    }
    return render(request,'staff/contact/detail.html',context)

@login_required
def deleteContact(request,pk):
    contact=Contact.objects.get(pk=pk)
    contact.delete()
    return redirect('list-contact')


#NEWS
@login_required
def listNews(request):
    newsList=News.objects.all()
    newsList=newsList.order_by('-news_date')
    context={
        'newsList':newsList
    }
    return render(request,'staff/news/list.html',context)

@method_decorator(login_required,name='dispatch')
class NewsUpdateView(UpdateView):
    model = News
    fields = '__all__'
    success_url = '/staff/list-news'
    template_name = 'staff/news/form.html'
@login_required
def deleteNews(request,pk):
    news=News.objects.get(pk=pk)
    news.delete()
    return redirect('list-news')

@method_decorator(login_required,name='dispatch')
class NewsCreateView(CreateView):
    model = News
    fields = '__all__'
    success_url = '/staff/list-news'
    template_name = 'staff/news/form.html'
