from django.urls import path
from .views import *

urlpatterns = [
    path('',index),
    path('search',searchProduct,name='search'),
    path('gioi-thieu',Introduce,name='gioi-thieu'),
    path('all-product',ViewAllProduct,name='all-product'),
    path('detail-product/<pk>',viewProductDetail,name='detail-product'),
    path('order-product/<pk>',orderProduct,name='order-product'),
    path('lien-he',ContactView,name='lien-he'),
    path('thank-you',ThankYou,name='thank-you'),
]