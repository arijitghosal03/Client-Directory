from django.db import models

# Create your models here.
class CustomerModel(models.Model):
    IMPORTER = 'importer'
    EXPORTER = 'exporter'
    CATEGORY_CHOICES = {
        IMPORTER: 'Importer',
        EXPORTER: 'Exporter',
    }
    customer_id = models.AutoField(primary_key=True)
    customer_name = models.CharField(max_length = 50)
    customer_category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(max_length=254, blank=True, null=True)
    socialmedia_link = models.URLField(max_length=200, blank=True, null=True)
    website_link = models.URLField(max_length=200, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    file_upload = models.FileField(upload_to='uploads/', blank=True, null=True)

