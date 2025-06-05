from django.db import models

# Create your models here

class Supplier(models.Model):
    name = models.CharField(max_length=100, blank=True, unique=True)
    code = models.CharField(max_length=50, blank=True, unique=True)
    email = models.EmailField(max_length=254, blank=True)
    mobile_phone = models.CharField(max_length=30, blank=True)
    address1 = models.CharField(max_length=255, blank=True)
    contact_name = models.CharField(max_length=100, blank=True)
    address2 = models.CharField(max_length=255, blank=True)
    tin = models.CharField(max_length=50, blank=True)
    address3 = models.CharField(max_length=255, blank=True)
    gst_exempt = models.CharField(max_length=50, blank=True)
    post_code = models.CharField(max_length=20, blank=True)
    bank = models.CharField(max_length=100, blank=True)
    phone_no = models.CharField(max_length=30, blank=True)
    bsb = models.CharField(max_length=20, blank=True)
    email2 = models.EmailField(max_length=254, blank=True)
    bank_account = models.CharField(max_length=50, blank=True)
    product = models.CharField(max_length=100, blank=True)
    bank_account_name = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"{self.code} - {self.name}"