from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm

from .models import Shop, Owner


class AuthForm(UserCreationForm):
    telephone = forms.CharField(max_length=255)
    shop_name = forms.CharField(max_length=255)
    shop_address = forms.CharField(max_length=255)

    class Meta:
        model = User
        fields = ['username', 'telephone', 'email', 'password1', 'password2', 'shop_name', 'shop_address']


class ShopForm(ModelForm):
    class Meta:
        model = Shop
        fields = 'name', 'address'


class OwnerForm(ModelForm):
    class Meta:
        model = Owner
        fields = ['name', 'telephone', 'email', 'shop']
