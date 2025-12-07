from django.contrib import admin
from .models import Inventory


@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin):
    """Admin interface for Inventory model."""
    
    list_display = ('product_name', 'product_sku', 'available_quantity', 'reserved_quantity', 'warehouse_location', 'is_low_stock')
    list_filter = ('warehouse_location',)
    search_fields = ('product_name', 'product_sku')
    ordering = ('product_name',)
    readonly_fields = ('updated_at',)
