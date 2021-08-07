from django import forms
from django.db import close_old_connections
from django.forms import fields
from django.forms.models import model_to_dict
from django.forms.widgets import PasswordInput
from django.template.defaultfilters import first
from .models import Post
from django.contrib.auth.models import User

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','body','status']


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput())

class UserCreateForm(forms.ModelForm):
    passwordagain = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields =['first_name','last_name','username','email','password','passwordagain']


            
