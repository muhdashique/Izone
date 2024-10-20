# forms.py
from django import forms
from .models import GalleryImage, Product
from IZONapp import models
from django.db import models 







class ProductForm(forms.ModelForm):

    
    class Meta:
        model = Product
        fields = ['name', 'description', 'price',  'image'] 



# forms.py


class LoginForm(forms.Form):
    username = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))


class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = GalleryImage
        fields = [ 'image']

class GalleryImageForm(forms.ModelForm):
    class Meta:
        model = GalleryImage
        fields = ['image']