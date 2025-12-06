from django.db import models


class Inventory(models.Model):
    """Model representing inventory/stock levels."""
    
    product_sku = models.CharField(max_length=100, unique=True)
    product_name = models.CharField(max_length=255)
    available_quantity = models.IntegerField(default=0)
    reserved_quantity = models.IntegerField(default=0)
    warehouse_location = models.CharField(max_length=255)
    low_stock_threshold = models.IntegerField(default=10)
    last_restocked = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name_plural = "Inventories"
        ordering = ['product_name']
    
    def __str__(self):
        return f"{self.product_name} - Available: {self.available_quantity}"
    
    @property
    def is_low_stock(self):
        return self.available_quantity <= self.low_stock_threshold
