from django.urls import path
from . import views

urlpatterns = [
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
    # path('product_detail/<int:product_id>/', views.product_detail, name='product_detail'),  # Updated for clarity
    path('products/category/<str:category>/', views.product_by_category, name='product_by_category'),
    path('careers/', views.careers, name='careers'),
    path('product_gallery/', views.product_gallery, name='product_gallery'),
   
    # path('product/<int:product_id>/', views.product_details, name='product_details'),
    path('product/<int:product_id>/delete/', views.delete_product, name='delete_product'),
    path('product/<int:product_id>/edit/', views.edit_product, name='edit_product'),
    path('gallery/edit/<int:image_id>/', views.edit_gallery_image, name='edit_gallery_image'),
    path('service/', views.service, name='service'),
    path('ProductItemDisplay/<int:id>/', views.ProductItemDisplay, name='ProductItemDisplay'),
    path('contact/', views.contact_form_view, name='contact'),
    path('logout/', views.logout_view, name='logout'),
    path('product_details/',views.product_details,name='product_details'),
    path('category/<str:category>/', views.product_by_category, name='product_by_category'),
    path('category/<str:category>/', views.product_by_category, name='product_by_category'),
    path('product/<int:product_id>/', views.product_details, name='product_detail'),
    path('product/image/<int:product_id>/', views.product_image_view, name='product_image_view'),
 ] 

