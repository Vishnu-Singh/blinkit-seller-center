from rest_framework import viewsets, filters, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from .models import Order, OrderItem
from .serializers import (
    OrderSerializer, 
    OrderListSerializer, 
    OrderStatusUpdateSerializer,
    OrderItemSerializer
)


class OrderViewSet(viewsets.ModelViewSet):
    """
    ViewSet for Order CRUD operations.
    
    Endpoints:
    - GET /api/orders/ - List all orders
    - POST /api/orders/ - Create a new order
    - GET /api/orders/{id}/ - Retrieve an order
    - PUT /api/orders/{id}/ - Update an order
    - PATCH /api/orders/{id}/ - Partial update an order
    - DELETE /api/orders/{id}/ - Delete an order
    - POST /api/orders/{id}/update_status/ - Update order status
    - GET /api/orders/pending/ - List pending orders
    """
    
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['status', 'payment_method']
    search_fields = ['order_id', 'customer_name', 'customer_phone']
    ordering_fields = ['order_date', 'total_amount']
    
    def get_serializer_class(self):
        """Return appropriate serializer based on action."""
        if self.action == 'list':
            return OrderListSerializer
        elif self.action == 'update_status':
            return OrderStatusUpdateSerializer
        return OrderSerializer
    
    @action(detail=True, methods=['post'])
    def update_status(self, request, pk=None):
        """Update order status."""
        order = self.get_object()
        serializer = OrderStatusUpdateSerializer(order, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @action(detail=False, methods=['get'])
    def pending(self, request):
        """Get all pending orders."""
        pending_orders = self.queryset.filter(status='pending')
        serializer = OrderListSerializer(pending_orders, many=True)
        return Response(serializer.data)
