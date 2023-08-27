from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class AuthForm(UserCreationForm):
    telephone = forms.CharField(max_length=255)

    class Meta:
        model = User
        fields = ['username', 'telephone', 'email', 'password1', 'password2']
