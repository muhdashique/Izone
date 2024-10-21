from django.contrib import admin
from django.urls import include, path
from .import views



urlpatterns = [
    # path('admin/', admin.site.urls),
    path('login/',views.login, name='login'),
    path('', views.home, name='home'),
    path('gallery/',views.gallery,name='gallery'),
    path('about/',views.about,name='about'),
    path('add-product/', views.add_product, name='add_product'),
    path('contactus/',views.contactus,name='contactus'),
  
    path('upload_image/', views.upload_image, name='upload_image'),
    path('gallery_list/', views.gallery_list, name='gallery_list'),


    # products
    # path('product_lap/', views.product_lap, name='laptop'),
    # path('product_desk/', views.product_desk, name='desktop'),
    # path('product_print/', views.product_print, name='printer'),
    # path('product_thermal/', views.product_thermal, name='thermal'),
    # path('product_barcod/', views.product_barcod, name='barcod'),
    # path('product_sccanner/', views.product_scanner, name='sccanner'),
    # path('product_cctv/', views.product_cctv, name='cctv'),
    # path('product_rollsribbon/', views.product_rollsribbon, name='rollsribbon'),
    # path('product_secusystem/', views.product_secusystem, name='secusyetem'),
    # path('product_accessories/', views.product_accessories, name='accessories'),
     
    #   path('', views.product_dropdown, name='home'), 

    
]