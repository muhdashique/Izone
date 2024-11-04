from itertools import product
from msilib.schema import ListView
from unicodedata import category
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
    products = Product.objects.all()  # Fetch all products

    return render(request, 'gallery.html', {'images': images, 'products': products})





# About page view
def about(request):
    products = Product.objects.all()  # Fetch all products

    return render(request, 'about.html',{'products': products})


# Product addition view
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product_gallery')  # Redirect to product gallery after saving
    else:
        form = ProductForm()
    
    return render(request, 'productadd.html', {'form': form})



def product_gallery(request):
    products = Product.objects.all()  # Retrieve all products
    return render(request, 'productgallery.html', {'products': products})






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
    products = Product.objects.all()  # Retrieve all products
    form = ProductForm()

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('productgallery.htmlt')  # Redirect to the same page after saving

    return render(request, 'product_details.html', {'products': products, 'form': form})





def delete_image(request, image_id):
    image = get_object_or_404(GalleryImage, id=image_id)
    if request.method == 'POST':
        image.delete()  # Delete the image
        return redirect('gallery')  # Redirect to gallery after deletion
    
    return render(request, 'confirm_delete.html', {'image': image})




def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'products.html', {'product': product})



from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.http import HttpResponse

def send_email(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        
        # Compose the email content
        subject = "New Enquiry Submission"
        message = f"Full Name: {name}\nEmail: {email}\nPhone: {phone}"
        from_email = 'your_email@example.com'
        recipient_list = ['recipient_email@example.com']  # Replace with your target email
        
        # Send the email
        send_mail(subject, message, from_email, recipient_list)
        
        # Redirect or render a success message
        return HttpResponse("Thank you for your enquiry. We'll get back to you soon!")
    
    # Render the correct template based on the referer
    referer = request.META.get('HTTP_REFERER', '')
    if 'contactus.html' in referer:
        return render(request, 'contactus.html')
    return render(request, 'about.html')



from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse
from .models import Product

def delete_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    product.delete()
    return redirect(reverse('product_gallery'))








def careers(request):
    products = Product.objects.all()  # Fetch all products

    return render (request,'career.html',{'products': products})

def product_details(request, product_id):
    products = Product.objects.all()
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'product_details.html', {'product': product, 'products': products})



from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from .forms import ProductForm

def edit_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_gallery')
    else:
        form = ProductForm(instance=product)
    return render(request, 'edit_product.html', {'form': form, 'product': product})

def product_gallery(request):
    products = Product.objects.all()
    return render(request, 'productgallery.html', {'products': products})

def delete_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        product.delete()
    return redirect('product_gallery')

def product_details(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'product_details.html', {'product': product})


