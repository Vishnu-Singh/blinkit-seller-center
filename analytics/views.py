from rest_framework import viewsets, filters, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Sum, Avg
from .models import SalesReport, ProductPerformance
from .serializers import (
    SalesReportSerializer, 
    SalesReportListSerializer, 
    ProductPerformanceSerializer,
    ProductPerformanceListSerializer
)


class SalesReportViewSet(viewsets.ModelViewSet):
    """
    ViewSet for SalesReport CRUD operations.
    
    Endpoints:
    - GET /api/sales-reports/ - List all sales reports
    - POST /api/sales-reports/ - Create a new sales report
    - GET /api/sales-reports/{id}/ - Retrieve a sales report
    - PUT /api/sales-reports/{id}/ - Update a sales report
    - PATCH /api/sales-reports/{id}/ - Partial update a sales report
    - DELETE /api/sales-reports/{id}/ - Delete a sales report
    - GET /api/sales-reports/summary/ - Get summary statistics
    """
    
    queryset = SalesReport.objects.all()
    serializer_class = SalesReportSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['date']
    ordering_fields = ['date', 'total_revenue', 'total_orders']
    
    def get_serializer_class(self):
        """Return appropriate serializer based on action."""
        if self.action == 'list':
            return SalesReportListSerializer
        return SalesReportSerializer
    
    @action(detail=False, methods=['get'])
    def summary(self, request):
        """Get summary statistics for all sales reports."""
        total_revenue = self.queryset.aggregate(Sum('total_revenue'))['total_revenue__sum'] or 0
        total_orders = self.queryset.aggregate(Sum('total_orders'))['total_orders__sum'] or 0
        avg_order_value = self.queryset.aggregate(Avg('average_order_value'))['average_order_value__avg'] or 0
        
        return Response({
            'total_revenue': total_revenue,
            'total_orders': total_orders,
            'average_order_value': round(avg_order_value, 2)
        })


class ProductPerformanceViewSet(viewsets.ModelViewSet):
    """
    ViewSet for ProductPerformance CRUD operations.
    
    Endpoints:
    - GET /api/product-performance/ - List all product performance reports
    - POST /api/product-performance/ - Create a new product performance report
    - GET /api/product-performance/{id}/ - Retrieve a product performance report
    - PUT /api/product-performance/{id}/ - Update a product performance report
    - PATCH /api/product-performance/{id}/ - Partial update a product performance report
    - DELETE /api/product-performance/{id}/ - Delete a product performance report
    - GET /api/product-performance/top_performers/ - Get top performing products
    """
    
    queryset = ProductPerformance.objects.all()
    serializer_class = ProductPerformanceSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['report_date', 'product_sku']
    search_fields = ['product_name', 'product_sku']
    ordering_fields = ['report_date', 'total_revenue', 'total_quantity_sold']
    
    def get_serializer_class(self):
        """Return appropriate serializer based on action."""
        if self.action == 'list':
            return ProductPerformanceListSerializer
        return ProductPerformanceSerializer
    
    @action(detail=False, methods=['get'])
    def top_performers(self, request):
        """Get top 10 performing products by revenue."""
        top_products = self.queryset.order_by('-total_revenue')[:10]
        serializer = ProductPerformanceSerializer(top_products, many=True)
        return Response(serializer.data)
