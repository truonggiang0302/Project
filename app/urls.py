from django.urls import path
from .views import *

urlpatterns = [
    path('',index),
    path('view-product',viewProduct,name='view-product'),
]