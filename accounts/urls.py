from django.urls import path
from .views import *

urlpatterns = [
    path('sign-up',signUp,name='sign-up'),
]