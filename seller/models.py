from django.db import models


class Seller(models.Model):
    """Model representing a seller account."""
    
    seller_id = models.CharField(max_length=100, unique=True)
    business_name = models.CharField(max_length=255)
    contact_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    address = models.TextField()
    gstin = models.CharField(max_length=15, help_text="GST Identification Number")
    pan = models.CharField(max_length=10, help_text="PAN Card Number")
    bank_account = models.CharField(max_length=20)
    bank_ifsc = models.CharField(max_length=11)
    is_active = models.BooleanField(default=True)
    is_verified = models.BooleanField(default=False)
    joined_date = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-joined_date']
    
    def __str__(self):
        return f"{self.business_name} ({self.seller_id})"
