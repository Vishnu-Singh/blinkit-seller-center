from rest_framework import serializers
from .models import SalesReport, ProductPerformance


class SalesReportSerializer(serializers.ModelSerializer):
    """Serializer for SalesReport model."""
    
    class Meta:
        model = SalesReport
        fields = '__all__'
        read_only_fields = ('created_at',)


class SalesReportListSerializer(serializers.ModelSerializer):
    """Lightweight serializer for sales report listings."""
    
    class Meta:
        model = SalesReport
        fields = ('id', 'date', 'total_orders', 'total_revenue', 'average_order_value')


class ProductPerformanceSerializer(serializers.ModelSerializer):
    """Serializer for ProductPerformance model."""
    
    class Meta:
        model = ProductPerformance
        fields = '__all__'


class ProductPerformanceListSerializer(serializers.ModelSerializer):
    """Lightweight serializer for product performance listings."""
    
    class Meta:
        model = ProductPerformance
        fields = ('id', 'product_name', 'total_quantity_sold', 'total_revenue', 'report_date')
