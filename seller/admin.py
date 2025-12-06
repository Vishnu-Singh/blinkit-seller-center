from django.contrib import admin
from .models import Seller


@admin.register(Seller)
class SellerAdmin(admin.ModelAdmin):
    """Admin interface for Seller model."""
    
    list_display = ('business_name', 'seller_id', 'email', 'phone', 'is_active', 'is_verified', 'joined_date')
    list_filter = ('is_active', 'is_verified', 'joined_date')
    search_fields = ('seller_id', 'business_name', 'email', 'phone', 'gstin', 'pan')
    ordering = ('-joined_date',)
    readonly_fields = ('joined_date', 'updated_at')
