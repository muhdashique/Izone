from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('gallery/', views.gallery, name='gallery'),
    path('about/', views.about, name='about'),
    path('add_product/', views.add_product, name='add_product'),
    path('contactus/', views.contactus, name='contactus'),
    path('login/', views.login, name='login'),
    path('upload_image/', views.upload_image, name='upload_image'),
    path('gallery_list/', views.gallery_list, name='gallery_list'),
    path('product_list/', views.product_list, name='product_list'),
    path('delete/<int:image_id>/', views.delete_image, name='delete_image'),
    path('products/', views.product_list, name='product_list'),
    path('product_detail/', views.product_detail, name='product_detail'),
    path('send-email/', views.send_email, name='send_email'),
    path('send-email/contactus/', views.send_email, {'template': 'contactus.html'}, name='send_email_contactus'),
    path('careers/', views.careers, name='careers'),
    path('product_gallery/', views.product_gallery, name='product_gallery'),
    path('product/<int:product_id>/', views.product_details, name='product_details'),  # Added missing comma
    path('product/gallery/', views.product_gallery, name='product_gallery'),
    path('product/<int:product_id>/details/', views.product_details, name='product_details'),
    path('product/<int:product_id>/delete/', views.delete_product, name='delete_product'),
    path('product/<int:product_id>/edit/', views.edit_product, name='edit_product'),
]
