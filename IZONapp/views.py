from email.message import EmailMessage
from itertools import product
from msilib.schema import ListView
from unicodedata import category
from urllib import request
from django.forms import Form
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import authenticate, login as auth_login
from IZONapp.forms import ProductForm, GalleryImageForm, LoginForm
from .models import  GalleryImage, LoginAttempt, Product
from django.contrib import messages
from msilib.schema import ListView


from django.shortcuts import get_object_or_404
from django.core.mail import send_mail
from django.shortcuts import render
# from django.template.defaultfilters import slugify


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
                return redirect('/')  # Redirect after successful login
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





# # Gallery view to display images
# def gallery(request):
#     images = GalleryImage.objects.all()  # Fetch all images
#     products = Product.objects.all()  # Fetch all products

#     return render(request, 'gallery.html', {'images': images, 'products': products})





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



# Product gallery view (list products by category)
# def product_gallery(request):
#     category = request.GET.get('category', None)
#     if category:
#         products = Product.objects.filter(category=category)
#     else:
#         products = Product.objects.all()

#     categories = [choice[0] for choice in Product.CATEGORY_CHOICES]
#     return render(request, 'productgallery.html', {'products': products, 'categories':categories})








# Contact Us page view
def contactus(request):
    return render(request, 'contactus.html')




# # Image upload for gallery
# def upload_image(request):
#     if request.method == 'POST':
#         form = GalleryImageForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()  # Save the image
#             return redirect('upload_image')  # Redirect to gallery after uploading
    
#     images = GalleryImage.objects.all()  # Fetch all images
#     form = GalleryImageForm()  # Empty form to show on page
    
#     return render(request, 'galleryadd.html', {'form': form, 'images': images})





# # Gallery list with image uploading
# def gallery_list(request):
#     if request.method == "POST":
#         form = GalleryImageForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()  # Save the image
#             return redirect('gallery')  # Redirect to gallery after uploading

#     images = GalleryImage.objects.all()  # Fetch all images
#     form = GalleryImageForm()  # Empty form for uploading
    
#     return render(request, 'gallery.html', {'form': form, 'images': images})




# Product list view
# def product_list(request):
#     products = Product.objects.all()  # Retrieve all products
#     form = ProductForm()

#     if request.method == 'POST':
#         form = ProductForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('productgallery.htmlt')  # Redirect to the same page after saving

#     return render(request, 'product_details.html', {'products': products, 'form': form})




# gallery image deleting view

# def delete_image(request, image_id):
#     image = get_object_or_404(GalleryImage, id=image_id)
#     if request.method == 'POST':
#         image.delete()  # Delete the image
#         return redirect('gallery')  # Redirect to gallery after deletion
    
#     return render(request, 'confirm_delete.html', {'image': image})




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


def product_by_category(request, category=None):
    # Get all categories
    categories = Product.objects.values_list('category', flat=True).distinct()
    
    # Get products for each category
    products_by_category = {cat: Product.objects.filter(category=cat) for cat in categories}

    # Use the provided category or the first category as the default
    selected_category = category if category else (categories[0] if categories else None)

    context = {
        'categories': categories,
        'products_by_category': products_by_category,
        'selected_category': selected_category,
    }
    
    return render(request, 'product_details.html', context)





from django.contrib.auth import logout
from django.shortcuts import redirect

def logout_view(request):
    logout(request)
    return redirect('home')  # Redirect to the home page or login page after logout


# from django.contrib import messages
# from django.shortcuts import render, redirect, get_object_or_404
# from django.urls import reverse
# from .models import Product

# def delete_product(request, product_id):
#     product = get_object_or_404(Product, id=product_id)  # Fetch product by ID or return 404 if not found
#     product.delete()  # Delete the product
#     return redirect('product_details')  # Redirect after deletion



def careers(request):
    products = Product.objects.all()  # Fetch all products
    return render (request,'career.html',{'products': products})



from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from .forms import ProductForm

def edit_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_details')
    else:
        form = ProductForm(instance=product)
    return render(request, 'edit_product.html', {'form': form, 'product': product})


# def edit_gallery_image(request, image_id):
#     image = get_object_or_404(GalleryImage, id=image_id)
#     if request.method == 'POST':
#         form = GalleryImageForm(request.POST, request.FILES, instance=image)
#         if form.is_valid():
#             form.save()
#             return redirect('upload_image')
#     else:
#         form = GalleryImageForm(instance=image)
#     return render(request, 'edit_gallery_image.html', {'form': form, 'image': image})


def product_gallery(request):
    products = Product.objects.all()
    return render(request, 'product_details.html', {'products': products})




def delete_product(request, product_id):
    # Fetch the product by id, or return 404 if not found
    product = get_object_or_404(Product, id=product_id)
    
    if request.method == 'POST':
        product.delete()  # Delete the product if the method is POST
    
    # Redirect to a page after deletion. For example, the product list or product details.
    return redirect('product_details')  # Adjust this to your desired redirect page




def service(request):
    return render(request,'service.html')



from django.template.loader import get_template

def ProductItemDisplay(request, id):
    product = get_object_or_404(Product, id=id)
    try:
        get_template('ProductItesmDisplay.html')
        print("Template found!")
    except Exception as e:
        print("Template error:", e)
    return render(request, 'ProductItemsDisplay.html', {'product': product})



def product_details(request):
    return render(request,'product_details.html')


def product_image_view(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    category_products = Product.objects.filter(category=product.category).order_by('id')
    product_ids = list(category_products.values_list('id', flat=True))

    current_index = product_ids.index(product_id)
    previous_product = category_products[current_index - 1] if current_index > 0 else None
    next_product = category_products[current_index + 1] if current_index < len(product_ids) - 1 else None

    context = {
        'product': product,
        'previous_product': previous_product,
        'next_product': next_product,
    }
    return render(request, 'ProductImageView.html', context)





def contact_form_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')  # Get phone number
        message = request.POST.get('message')

        if not all([name, email, phone, message]):
            messages.error(request, "All fields are required.")
            return redirect('contactus')

        try:
            send_mail(
                subject=f"New Contact Form Submission from {name}",
                message=(
                    f"Name: {name}\n"
                    f"Email: {email}\n"
                    f"Phone: {phone}\n\n"
                    f"Message:\n{message}"
                ),
                from_email='your_email@gmail.com',
                recipient_list=['muhammedashique8281@gmail.com'],
                fail_silently=False,
            )
            
            # Add a success message
            messages.success(request, "Your message has been sent successfully!")
            return redirect('contactus')
        
        except Exception as e:
            messages.error(request, f"An error occurred: {str(e)}")
            return redirect('contactus')

    return render(request, 'contactus.html')




# from django.shortcuts import render
# from .forms import ProductForm  # Assuming you have a ProductForm for adding products

# def product_add(request):
#     if request.method == 'POST':
#         form = ProductForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('product_details')  # Redirect to product details after successful addition
#     else:
#         form = ProductForm()

#     return render(request, 'product_add', {'form': form})  # Make sure the path is correct



def product_page(request):
    # Add the necessary logic to fetch and display products
    return render(request, 'productdetails.html')




