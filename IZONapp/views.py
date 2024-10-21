# views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login

from IZONapp.forms import ProductForm
from .forms import GalleryImageForm, LoginForm
from .models import GalleryImage, LoginAttempt
from .models import Product




# login_fuction

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
                login_attempt.user = user  # Associate the user with the login attempt
                login_attempt.save()
                return redirect('add_product')  # Change this to your actual home URL name
            else:
                login_attempt.save()  # Save the failed attempt
                return render(request, 'login.html', {'form': form, 'error_message': 'Invalid username or password'})
    else:
        form = LoginForm()
    
    return render(request, 'login.html', {'form': form})





def home(request):
    products = Product.objects.all()
    return render(request, 'home.html', {'products': products})



def gallery(request):
    images = GalleryImage.objects.all()  # Fetch all images
    return render(request, 'gallery.html', {'images': images})



def about(request):
    return render(request, 'about.html')



# product_adding

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  
    else:
        form = ProductForm()
    
    return render(request, 'productadd.html', {'form': form})



def contactus(request):
    return render(request,'contactus.html')




def upload_image(request):
    if request.method == 'POST':
        form = GalleryImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('gallery')  

   
    images = GalleryImage.objects.all()

   
    form = GalleryImageForm()

    return render(request, 'galleryadd.html', {'form': form, 'images': images})  



def gallery_list(request):
    if request.method == "POST":
        form = GalleryImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('gallery')  
        form = GalleryImageForm()

    images = GalleryImage.objects.all()  
    return render(request, 'gallery.html', {'form': form, 'images': images})