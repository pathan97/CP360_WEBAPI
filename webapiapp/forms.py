from django.db import *
from django import forms
from django.forms import ModelForm
from .models import *

class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','password','email','role']

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['category_id','name','description','price','status']