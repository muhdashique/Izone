from django.contrib import admin
from django.urls import include, path
from .import views



urlpatterns = [
    # path('admin/', admin.site.urls),
    
    path('', views.home, name='home'),
    path('gallery/',views.gallery,name='gallery'),
    path('about/',views.about,name='about'),
    path('add_product/', views.add_product, name='add_product'),
    path('contactus/',views.contactus,name='contactus'),
    path('login/',views.login, name='login'),
    path('upload_image/', views.upload_image, name='upload_image'),
    path('gallery_list/', views.gallery_list, name='gallery_list'),
    
   path('product_list/', views.product_list, name='product_list'), 
  

   

    
]