from django.urls import path
from .views import *

urlpatterns = [
    #path('',index),
    path('',index1,name='index1'),
    path('search',searchProduct,name='search'),
    path('gioi-thieu',Introduce,name='gioi-thieu'),
    path('all-product',ViewAllProduct,name='all-product'),
    path('detail-product/<pk>',viewProductDetail,name='detail-product'),
    path('order-product/<pk>',orderProduct,name='order-product'),
    path('lien-he',ContactView,name='lien-he'),
    path('thank-you',ThankYou,name='thank-you'),
    path('thank-you1',ThankYou1,name='thank-you1'),
    path('tin-tuc',NewsView,name='news'),
    path('tin-tuc/<pk>',NewsDetailView,name='newsdetail'),
]