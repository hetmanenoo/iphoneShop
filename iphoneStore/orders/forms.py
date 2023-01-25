from django import forms
from .models import Order


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ["first_name", "last_name", "email", "address", "postal_code", "city"]
        # label = {'first_name':'І\'мя',
        #          'last_name':'Прізвище',
        #          'email':'Email',
        #          'address':'Адреса',
        #          'postal_code':'Поштовий індекс',
        #          'city':'Місто'
        #          }
