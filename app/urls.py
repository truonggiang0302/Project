from django.urls import path
from .views import *

urlpatterns = [
    path('',index),
    path('all-product',viewAllProduct,name='all-product'),
    path('honda',Honda,name='honda'),
    path('product/<pk>',viewProduct,name='product'),
    path('detail-product/<pk>',viewProductDetail,name='detail-product'),
    path('order-product/<pk>',orderProduct,name='order-product'),
]