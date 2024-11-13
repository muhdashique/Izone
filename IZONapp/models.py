from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone

class LoginAttempt(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True, blank=True)
    username_attempted = models.CharField(max_length=150)
    timestamp = models.DateTimeField(default=timezone.now)
    successful = models.BooleanField(default=False)

    def __str__(self):
        return f"Login attempt by {self.username_attempted} on {self.timestamp}"

# class Category(models.Model):
#     name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Product(models.Model):
    CATEGORY_CHOICES = [
        ('DESKTOP', 'DESKTOP'),
        ('LAPTOPS', ' LAPTOPS'),
        ('PRINTERS', 'PRINTERS'),
        ('SCANNERS ', 'SCANNERS '),
        (' CCTV', ' CCTV'),
        ('ROLLS AND RIBBONS', 'ROLLS AND RIBBONS'),
        ('SECURITY SYSTEM', 'SECURITY SYSTEM'),       
        ('ACCESSORIES', 'ACCESSORIES'),
       
        # Add more categories as needed
    ]

    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='product_images/', blank=True, null=True)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)

    def str(self):
        return self.name 


class GalleryImage(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title or "Gallery Image"

class ImageUpload(models.Model):
    image = models.ImageField(upload_to='images/')  # Ensure this is correct

    def __str__(self):
        return f"ImageUpload {self.id}"  # Just to provide a string representation
    


    from django.db import models

class Image(models.Model):
    # your model fields here
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=200)
    # other fields...

    def __str__(self):
        return self.title





