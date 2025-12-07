from rest_framework import viewsets, filters, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from .models import Inventory
from .serializers import (
    InventorySerializer, 
    InventoryListSerializer, 
    InventoryUpdateSerializer
)


class InventoryViewSet(viewsets.ModelViewSet):
    """
    ViewSet for Inventory CRUD operations.
    
    Endpoints:
    - GET /api/inventory/ - List all inventory items
    - POST /api/inventory/ - Create a new inventory item
    - GET /api/inventory/{id}/ - Retrieve an inventory item
    - PUT /api/inventory/{id}/ - Update an inventory item
    - PATCH /api/inventory/{id}/ - Partial update an inventory item
    - DELETE /api/inventory/{id}/ - Delete an inventory item
    - GET /api/inventory/low_stock/ - List low stock items
    - POST /api/inventory/{id}/update_stock/ - Update stock levels
    """
    
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['warehouse_location']
    search_fields = ['product_sku', 'product_name']
    ordering_fields = ['available_quantity', 'updated_at']
    
    def get_serializer_class(self):
        """Return appropriate serializer based on action."""
        if self.action == 'list':
            return InventoryListSerializer
        elif self.action == 'update_stock':
            return InventoryUpdateSerializer
        return InventorySerializer
    
    @action(detail=False, methods=['get'])
    def low_stock(self, request):
        """Get all low stock items."""
        low_stock_items = [item for item in self.queryset.all() if item.is_low_stock]
        serializer = InventoryListSerializer(low_stock_items, many=True)
        return Response(serializer.data)
    
    @action(detail=True, methods=['post'])
    def update_stock(self, request, pk=None):
        """Update stock levels."""
        inventory = self.get_object()
        serializer = InventoryUpdateSerializer(inventory, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
