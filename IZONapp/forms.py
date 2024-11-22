# forms.py
from django import forms
from .models import GalleryImage, Product
from IZONapp import models
from django.db import models 


class ProductForm(forms.ModelForm):
    
    # You can add a field for category image if required
    category_image = forms.ImageField(required=False, widget=forms.ClearableFileInput(attrs={'class': 'form-control'}))
    
    # Adding a select field for categories
    category = forms.ChoiceField(choices=Product.CATEGORY_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = Product
        fields = ['name','model_name', 'brand_name', 'description', 'price', 'image', 'category', 'category_image']

    def _init_(self, *args, **kwargs):
        super(ProductForm, self)._init_(*args, **kwargs)
        # Optionally, you can add a default value for category_image from model method
        # This will be set for the category's default image if no image is uploaded.
        if self.instance and not self.instance.category_image:
            self.fields['category_image'].initial = self.instance.get_category_image()
     

class LoginForm(forms.Form):
    username = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))

class GalleryImageForm(forms.ModelForm):
    class Meta:
        model = GalleryImage
        fields = ['title', 'description', 'image']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'image': forms.FileInput(attrs={'class': 'form-control'})
        }