from django.urls import path
from .views import *

urlpatterns = [
    path('',index),
    path('all-product',viewAllProduct,name='all-product'),
    path('product/<pk>',viewProduct,name='product'),
    path('detail-product/<pk>',viewProductDetail,name='detail-product'),
]