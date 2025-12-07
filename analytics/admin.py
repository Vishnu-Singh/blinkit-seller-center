from django.contrib import admin
from .models import SalesReport, ProductPerformance


@admin.register(SalesReport)
class SalesReportAdmin(admin.ModelAdmin):
    """Admin interface for SalesReport model."""
    
    list_display = ('date', 'total_orders', 'total_revenue', 'average_order_value', 'created_at')
    list_filter = ('date',)
    ordering = ('-date',)
    readonly_fields = ('created_at',)


@admin.register(ProductPerformance)
class ProductPerformanceAdmin(admin.ModelAdmin):
    """Admin interface for ProductPerformance model."""
    
    list_display = ('product_name', 'product_sku', 'total_quantity_sold', 'total_revenue', 'report_date')
    list_filter = ('report_date',)
    search_fields = ('product_name', 'product_sku')
    ordering = ('-report_date', '-total_revenue')
