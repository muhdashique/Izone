from itertools import product
from msilib.schema import ListView
from django.forms import Form
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import authenticate, login as auth_login
from IZONapp.forms import ProductForm, GalleryImageForm, LoginForm
from .models import  GalleryImage, LoginAttempt, Product




# Login view with login attempt logging
def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)

            # Log the login attempt
            login_attempt = LoginAttempt(username_attempted=username, successful=user is not None)

            if user is not None:
                auth_login(request, user)
                login_attempt.user = user  # Attach user if authentication succeeds
                login_attempt.save()
                return redirect('add_product')  # Redirect after successful login
            else:
                login_attempt.save()  # Save failed login attempt
                return render(request, 'login.html', {'form': form, 'error_message': 'Invalid username or password'})
    else:
        form = LoginForm()
    
    return render(request, 'login.html', {'form': form})




# Home view to display products
def home(request):
    products = Product.objects.all()  # Fetch all products
    return render(request, 'home.html', {'products': products})





# Gallery view to display images
def gallery(request):
    images = GalleryImage.objects.all()  # Fetch all images
    return render(request, 'gallery.html', {'images': images})





# About page view
def about(request):
    return render(request, 'about.html')


# Product addition view
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()  # Save the product
            return redirect('home')  # Redirect to home or products list
    else:
        form = ProductForm()
    
    return render(request, 'productadd.html', {'form': form})






# Contact Us page view
def contactus(request):
    return render(request, 'contactus.html')




# Image upload for gallery
def upload_image(request):
    if request.method == 'POST':
        form = GalleryImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()  # Save the image
            return redirect('gallery')  # Redirect to gallery after uploading
    
    images = GalleryImage.objects.all()  # Fetch all images
    form = GalleryImageForm()  # Empty form to show on page
    
    return render(request, 'galleryadd.html', {'form': form, 'images': images})





# Gallery list with image uploading
def gallery_list(request):
    if request.method == "POST":
        form = GalleryImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()  # Save the image
            return redirect('gallery')  # Redirect to gallery after uploading

    images = GalleryImage.objects.all()  # Fetch all images
    form = GalleryImageForm()  # Empty form for uploading
    
    return render(request, 'gallery.html', {'form': form, 'images': images})




# Product list view
def product_list(request):
    products = Product.objects.all() 
    return render(request, 'products.html', {'products': products})