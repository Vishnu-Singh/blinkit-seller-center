from django.contrib import admin
from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """Admin interface for Product model."""
    
    list_display = ('name', 'sku', 'price', 'status', 'category', 'brand', 'created_at')
    list_filter = ('status', 'category', 'brand')
    search_fields = ('name', 'sku', 'description')
    ordering = ('-created_at',)
    readonly_fields = ('created_at', 'updated_at')
