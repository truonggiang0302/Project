from datetime import datetime
from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.views.generic.edit import CreateView, UpdateView
from django.utils.decorators import method_decorator
from django.conf import settings
import math
from django.contrib.auth.decorators import login_required


def listCategory(request):
    categoryList = Category.objects.all()
    context = {'categoryList': categoryList}
    return render(request, 'staff/category/list.html', context)
