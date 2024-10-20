# views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login

from IZONapp.forms import ProductForm
from .forms import GalleryImageForm, LoginForm
from .models import GalleryImage, LoginAttempt

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
    return render(request, 'home.html')



def product_lap(request):
    return render(request, 'product/laptop.html') 



def product_desk(request):
    return render(request, 'product/desktop.html')



def product_print(request):
    return render(request, 'product/printer.html')



def product_thermal(request):
    return render(request, 'product/theprint.html')


def product_barcod(request):
    return render(request, 'product/barprinter.html')


def product_scanner(request):
    return render(request, 'product/scanner.html')




def product_cctv(request):
    return render(request, 'product/cctv.html')




def product_rollsribbon(request):
    return render(request, 'product/rollsribbon.html')



def product_secusystem(request):
    return render(request, 'product/secusystem.html')




def product_accessories(request):
    return render(request, 'product/accessories.html')



def gallery(request):
    return render(request, 'gallery.html')



def about(request):
    return render(request, 'about.html')





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



from django.shortcuts import render, redirect
from .models import GalleryImage
from .forms import GalleryImageForm

def upload_image(request):
    if request.method == 'POST':
        form = GalleryImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('gallery')  # Redirect to the gallery page after upload

    # Retrieve all gallery images
    images = GalleryImage.objects.all()

   
    form = GalleryImageForm()

    return render(request, 'galleryadd.html', {'form': form, 'images': images})  



def gallery_list(request):
    if request.method == "POST":
        form = GalleryImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('gallery')  # Redirect after saving to prevent duplicate submissions
    else:
        form = GalleryImageForm()

    images = GalleryImage.objects.all()  # Fetch all uploaded images
    return render(request, 'gallery.html', {'form': form, 'images': images})