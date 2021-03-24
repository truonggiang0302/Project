from django import forms
from .models import *
from .views import *


class OrderForm(forms.Form):
    qty = forms.IntegerField(min_value=1)
    customer_name = forms.CharField()
    customer_phone = forms.CharField()
    customer_address = forms.CharField()


    def clean_qty(self):
        product_Id =self.cleaned_data.get('qty')
        product = Product.objects.get(pk=1)
        if product_Id >product.qty:
            raise forms.ValidationError('Quá số lượng có trong cửa hàng')
        return product_Id


class ContactForm(forms.Form):
    customer_name = forms.CharField()
    customer_email = forms.EmailField()
    customer_phone = forms.CharField()
    customer_content = forms.CharField(widget=forms.Textarea)
