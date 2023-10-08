from django import forms 
from django.contrib.auth.models import User

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1']

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    email = forms.EmailInput()

    password = forms.CharField(widget=forms.PasswordInput())
