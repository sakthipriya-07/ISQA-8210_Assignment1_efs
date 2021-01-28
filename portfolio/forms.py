from django import forms
from .models import Customer, Stock, Investment, Mutual
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('cust_number', 'name', 'address', 'city', 'state', 'zipcode', 'email', 'cell_phone',)


class StockForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ('customer', 'symbol', 'name', 'shares', 'purchase_price', 'purchase_date',)


class InvestmentForm(forms.ModelForm):
    class Meta:
        model = Investment
        fields = ('customer', 'category', 'description', 'acquired_value', 'acquired_date', 'recent_value',
                  'recent_date',)


class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class MutualForm(forms.ModelForm):
    class Meta:
        model = Mutual
        fields = ('customer', 'fund_category', 'description', 'direct_plan', 'regular_plan', 'difference', 'acquired_date',)
