from django.urls import path
from .views import *

urlpatterns = [
    path('',index),
    path('view-all-product',viewAllProduct,name='view-all-product'),
    path('view-product',viewProduct,name='view-product'),
]