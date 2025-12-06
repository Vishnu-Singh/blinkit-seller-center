from django.contrib import admin
from .models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    """Inline admin for OrderItem."""
    model = OrderItem
    extra = 1


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    """Admin interface for Order model."""
    
    list_display = ('order_id', 'customer_name', 'total_amount', 'status', 'order_date')
    list_filter = ('status', 'payment_method', 'order_date')
    search_fields = ('order_id', 'customer_name', 'customer_phone')
    ordering = ('-order_date',)
    readonly_fields = ('order_date', 'updated_at')
    inlines = [OrderItemInline]


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    """Admin interface for OrderItem model."""
    
    list_display = ('order', 'product_name', 'quantity', 'unit_price', 'total_price')
    search_fields = ('product_name', 'product_sku')
