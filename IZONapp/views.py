from itertools import product
from msilib.schema import ListView
from unicodedata import category
from django.forms import Form
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import authenticate, login as auth_login
from IZONapp.forms import ProductForm, GalleryImageForm, LoginForm
from .models import  GalleryImage, LoginAttempt, Product
from django.contrib import messages
from django.conf import settings
from django.template.loader import render_to_string
from django.utils.html import strip_tags



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

    return render(request, 'productadd.html',{'form':form})


# Product addition view
# def add_product(request):
#     if request.method == 'POST':
#         form = ProductForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('product_gallery')  # Redirect to product gallery after saving
#     else:
#         form = ProductForm()
    
#     return render(request, 'productadd.html', {'form': form})


# Product gallery view (list products by category)
def product_gallery(request):
    category = request.GET.get('category', None)
    if category:
        products = Product.objects.filter(category=category)
    else:
        products = Product.objects.all()

    categories = [choice[0] for choice in Product.CATEGORY_CHOICES]
    return render(request, 'productgallery.html', {'products': products, 'categories':categories})



# def product_gallery(request):
#     products = Product.objects.all()  # Retrieve all products
#     return render(request, 'productgallery.html', {'products': products})






# Contact Us page view
def contactus(request):
    return render(request, 'contactus.html')




# Image upload for gallery
def upload_image(request):
    if request.method == 'POST':
        form = GalleryImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()  # Save the image
            return redirect('upload_image')  # Redirect to gallery after uploading
    
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




# gallery image deleting view

def delete_image(request, image_id):
    image = get_object_or_404(GalleryImage, id=image_id)
    if request.method == 'POST':
        image.delete()  # Delete the image
        return redirect('gallery')  # Redirect to gallery after deletion
    
    return render(request, 'confirm_delete.html', {'image': image})


def get_categories(request):
    # Get unique categories from products
    categories = Product.objects.values_list('category', flat=True).distinct()
    products_by_category = {}
    for category in categories:
        products_by_category[category] = Product.objects.filter(category=category)
    return {'categories': categories, 'products_by_category': products_by_category}

def base_context(request):
    # Context processor to make categories available in all templates
    return get_categories(request)
def product_by_category(request, category):
    products = Product.objects.filter(category=category)
    
    # Add the full image URL for each product
    for product in products:
        product.full_image_url = request.build_absolute_uri(product.image.url)
    
    return render(request, 'product_details.html', {
        'products': products,
        'selected_category': category,
        **get_categories(request)})



def product_details(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'product_details.html', {'product': product,**get_categories(request)})




def product_detail(request, product_id):
    products = Product.objects.all()  # Retrieve all products
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'products.html', {'product': product})



from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.http import HttpResponse
def send_email(request):
    if request.method == 'POST':
        try:
            # Get form data
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            phone = request.POST.get('phone', '')
            subject = request.POST.get('subject', '')
            message = request.POST.get('message', '')
            
            # Create HTML email content
            html_message = render_to_string('about.html', {
                'name': name,
                'email': email,
                'phone': phone,
                'subject': subject,
                'message': message
            })
            
            # Strip HTML for plain text version
            plain_message = strip_tags(html_message)
            
            # Send the email
            send_mail(
                subject=f"New Contact Form Submission: {subject}",
                message=plain_message,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[settings.ADMIN_EMAIL],
                html_message=html_message,
                fail_silently=False,
            )
            
            messages.success(request, 'Your message has been sent successfully!')
            return redirect('contact_success')
            
        except Exception as e:
            messages.error(request, 'There was an error sending your message. Please try again later.')
            return render(request, 'contact.html')
    
    return render(request, 'contact.html')



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


def edit_gallery_image(request, image_id):
    image = get_object_or_404(GalleryImage, id=image_id)
    if request.method == 'POST':
        form = GalleryImageForm(request.POST, request.FILES, instance=image)
        if form.is_valid():
            form.save()
            return redirect('upload_image')
    else:
        form = GalleryImageForm(instance=image)
    return render(request, 'edit_gallery_image.html', {'form': form, 'image': image})


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



def service(request):
    return render(request,'service.html')





from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib import messages

def contact_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        full_message = f"From: {email}\n\nMessage:\n{message}"
        
        # Send email
        try:
            send_mail(
                subject,
                full_message,
                settings.EMAIL_HOST_USER,
                ['muhammedashique8281@gmail.com'],  # Replace with your destination email
                fail_silently=False,
            )
            messages.success(request, "Your message has been sent successfully!")
            return redirect('contactus')
        except Exception as e:
            messages.error(request, "There was an error sending your message. Please try again later.")
    
    return render(request, 'contactus.html')

def ProductItemDisplay(request, product_id):
    # Retrieve all products (if you still need them for any purpose)
    products = Product.objects.all()
    # Retrieve the specific product by its ID
    product = get_object_or_404(Product, id=product_id)
    # Render the ProductItemDisplay.html template with the selected product
    return render(request, 'ProductItemDisplay.html', {'product': product})