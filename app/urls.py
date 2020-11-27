from django.urls import path
from .views import *

urlpatterns = [
    path('',index),
    path('search',searchProduct,name='search'),
    path('gioi-thieu',Introduce,name='gioi-thieu'),
    path('all-product',viewAllProduct,name='all-product'),
    path('honda',Honda,name='honda'),
    path('yamaha',Yamaha,name='yamaha'),
    path('ducati',Ducati,name='ducati'),
    path('kawasaki',Kawasaki,name='kawasaki'),
    path('bmw',BMW,name='bmw'),
    path('suzuki',Suzuki,name='suzuki'),
    path('ktm',KTM,name='ktm'),
    path('detail-product/<pk>',viewProductDetail,name='detail-product'),
    path('order-product/<pk>',orderProduct,name='order-product'),
    path('lien-he',Contact,name='lien-he'),
    path('thank-you',ThankYou,name='thank-you'),
]