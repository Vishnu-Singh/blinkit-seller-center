from django.db import models


class SalesReport(models.Model):
    """Model representing sales analytics and reports."""
    
    date = models.DateField()
    total_orders = models.IntegerField(default=0)
    total_revenue = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    total_items_sold = models.IntegerField(default=0)
    average_order_value = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    cancelled_orders = models.IntegerField(default=0)
    returned_orders = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-date']
        unique_together = ['date']
    
    def __str__(self):
        return f"Sales Report - {self.date}"


class ProductPerformance(models.Model):
    """Model representing product performance metrics."""
    
    product_sku = models.CharField(max_length=100)
    product_name = models.CharField(max_length=255)
    total_quantity_sold = models.IntegerField(default=0)
    total_revenue = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    view_count = models.IntegerField(default=0)
    conversion_rate = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    report_date = models.DateField()
    
    class Meta:
        ordering = ['-report_date', '-total_revenue']
    
    def __str__(self):
        return f"{self.product_name} - {self.report_date}"
