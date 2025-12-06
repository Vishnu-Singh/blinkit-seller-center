from rest_framework import viewsets, filters, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from .models import Seller
from .serializers import (
    SellerSerializer, 
    SellerListSerializer, 
    SellerCreateUpdateSerializer
)


class SellerViewSet(viewsets.ModelViewSet):
    """
    ViewSet for Seller CRUD operations.
    
    Endpoints:
    - GET /api/sellers/ - List all sellers
    - POST /api/sellers/ - Create a new seller
    - GET /api/sellers/{id}/ - Retrieve a seller
    - PUT /api/sellers/{id}/ - Update a seller
    - PATCH /api/sellers/{id}/ - Partial update a seller
    - DELETE /api/sellers/{id}/ - Delete a seller
    - POST /api/sellers/{id}/verify/ - Verify a seller
    - GET /api/sellers/active/ - List active sellers
    """
    
    queryset = Seller.objects.all()
    serializer_class = SellerSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['is_active', 'is_verified']
    search_fields = ['seller_id', 'business_name', 'email', 'phone']
    ordering_fields = ['joined_date', 'business_name']
    
    def get_serializer_class(self):
        """Return appropriate serializer based on action."""
        if self.action == 'list':
            return SellerListSerializer
        elif self.action in ['create', 'update', 'partial_update']:
            return SellerCreateUpdateSerializer
        return SellerSerializer
    
    @action(detail=True, methods=['post'])
    def verify(self, request, pk=None):
        """Verify a seller account."""
        seller = self.get_object()
        seller.is_verified = True
        seller.save()
        return Response({'status': 'seller verified'}, status=status.HTTP_200_OK)
    
    @action(detail=False, methods=['get'])
    def active(self, request):
        """Get all active sellers."""
        active_sellers = self.queryset.filter(is_active=True)
        serializer = SellerListSerializer(active_sellers, many=True)
        return Response(serializer.data)
