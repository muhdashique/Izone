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
    
from django.db import models

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('DESKTOP', 'DESKTOP'),
        ('LAPTOPS', 'LAPTOPS'),
        ('PRINTERS', 'PRINTERS'),
        ('SCANNERS', 'SCANNERS'),
        ('CCTV', 'CCTV'),
        ('ROLLS AND RIBBONS', 'ROLLS AND RIBBONS'),
        ('SECURITY SYSTEM', 'SECURITY SYSTEM'),
        ('ACCESSORIES', 'ACCESSORIES'),
    ]

    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='product_images/', blank=True, null=True)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    
    # Default category image setup based on category choice
    category_image = models.ImageField(upload_to='category_images/', blank=True, null=True)

    def _str_(self):  # Corrected method name
        return self.name

    # Method to return default category image
    def get_category_image(self):
        # You can set up a default image based on the category if category_image is not provided
        default_images = {
            'DESKTOP': 'https://res.cloudinary.com/dqydgc2ky/image/upload/v1731912582/WhatsApp_Image_2024-11-18_at_12.16.49_b23417a0_q7jag7.jpg',
            'LAPTOPS': 'https://res.cloudinary.com/dqydgc2ky/image/upload/v1731912589/WhatsApp_Image_2024-11-18_at_12.17.04_fe72f824_ffx5os.jpg',
            'PRINTERS': 'https://res.cloudinary.com/dqydgc2ky/image/upload/v1731912597/WhatsApp_Image_2024-11-18_at_12.17.18_af0cd42c_v4dj9k.jpg',
            'SCANNERS': 'https://res.cloudinary.com/dqydgc2ky/image/upload/v1731912606/WhatsApp_Image_2024-11-18_at_12.17.32_a1eba844_ddjsb6.jpg',
            'CCTV': 'https://res.cloudinary.com/dqydgc2ky/image/upload/v1731912611/WhatsApp_Image_2024-11-18_at_12.17.38_ed002cec_hxvl9s.jpg',
            'ROLLS AND RIBBONS': 'https://res.cloudinary.com/dqydgc2ky/image/upload/v1732085707/WhatsApp_Image_2024-11-20_at_12.16.46_ee3b529e_fqthyy.jpg',
            'SECURITY SYSTEM': 'https://res.cloudinary.com/dqydgc2ky/image/upload/v1732086126/WhatsApp_Image_2024-11-20_at_12.29.58_57cc4c56_jozqc4.jpg',
            'ACCESSORIES': 'https://res.cloudinary.com/dqydgc2ky/image/upload/v1732085712/WhatsApp_Image_2024-11-20_at_12.16.47_1b15d9e8_ght9ei.jpg',
        }

        # Return the corresponding default image path
        if self.category_image:
            return self.category_image.url  # Use the uploaded image if available
        else:
            return default_images.get(self.category, 'https://res.cloudinary.com/dqydgc2ky/image/upload/v1731912582/WhatsApp_Image_2024-11-18_at_12.16.49_b23417a0_q7jag7.jpg')  # Fallback to the default image if no match is found


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





