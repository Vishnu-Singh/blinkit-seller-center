from django.contrib import admin
from .models import Category, Brand


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Admin interface for Category model."""
    
    list_display = ('name', 'parent_category', 'is_active', 'display_order', 'created_at')
    list_filter = ('is_active', 'parent_category')
    search_fields = ('name', 'description')
    ordering = ('display_order', 'name')
    readonly_fields = ('created_at', 'updated_at')


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    """Admin interface for Brand model."""
    
    list_display = ('name', 'is_active', 'created_at')
    list_filter = ('is_active',)
    search_fields = ('name', 'description')
    ordering = ('name',)
    readonly_fields = ('created_at',)
