from rest_framework import viewsets, filters, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from .models import Product
from .serializers import (
    ProductSerializer, 
    ProductListSerializer, 
    ProductCreateUpdateSerializer
)


class ProductViewSet(viewsets.ModelViewSet):
    """
    ViewSet for Product CRUD operations.
    
    Endpoints:
    - GET /api/products/ - List all products
    - POST /api/products/ - Create a new product
    - GET /api/products/{id}/ - Retrieve a product
    - PUT /api/products/{id}/ - Update a product
    - PATCH /api/products/{id}/ - Partial update a product
    - DELETE /api/products/{id}/ - Delete a product
    - GET /api/products/active/ - List active products
    - POST /api/products/{id}/deactivate/ - Deactivate a product
    """
    
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['status', 'category', 'brand']
    search_fields = ['name', 'sku', 'description']
    ordering_fields = ['created_at', 'price', 'name']
    
    def get_serializer_class(self):
        """Return appropriate serializer based on action."""
        if self.action == 'list':
            return ProductListSerializer
        elif self.action in ['create', 'update', 'partial_update']:
            return ProductCreateUpdateSerializer
        return ProductSerializer
    
    @action(detail=False, methods=['get'])
    def active(self, request):
        """Get all active products."""
        active_products = self.queryset.filter(status='active')
        serializer = ProductListSerializer(active_products, many=True)
        return Response(serializer.data)
    
    @action(detail=True, methods=['post'])
    def deactivate(self, request, pk=None):
        """Deactivate a product."""
        product = self.get_object()
        product.status = 'inactive'
        product.save()
        return Response({'status': 'product deactivated'}, status=status.HTTP_200_OK)
