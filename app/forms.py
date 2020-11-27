from django import forms
from .models import *

class OrderForm(forms.Form):
    qty=forms.IntegerField(min_value=1)
    customer_name=forms.CharField()
    customer_phone=forms.CharField()
    customer_address=forms.CharField()

class ContactForm(forms.Form):
    customer_name=forms.CharField()
    customer_email=forms.EmailField()
    customer_phone=forms.CharField()
    customer_content=forms.CharField(widget=forms.Textarea)