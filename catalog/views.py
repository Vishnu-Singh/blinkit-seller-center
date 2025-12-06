from rest_framework import viewsets, filters, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from .models import Category, Brand
from .serializers import (
    CategorySerializer, 
    CategoryListSerializer, 
    BrandSerializer,
    BrandListSerializer
)


class CategoryViewSet(viewsets.ModelViewSet):
    """
    ViewSet for Category CRUD operations.
    
    Endpoints:
    - GET /api/categories/ - List all categories
    - POST /api/categories/ - Create a new category
    - GET /api/categories/{id}/ - Retrieve a category
    - PUT /api/categories/{id}/ - Update a category
    - PATCH /api/categories/{id}/ - Partial update a category
    - DELETE /api/categories/{id}/ - Delete a category
    - GET /api/categories/root/ - List root categories
    """
    
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['is_active', 'parent_category']
    search_fields = ['name', 'description']
    ordering_fields = ['display_order', 'name', 'created_at']
    
    def get_serializer_class(self):
        """Return appropriate serializer based on action."""
        if self.action == 'list':
            return CategoryListSerializer
        return CategorySerializer
    
    @action(detail=False, methods=['get'])
    def root(self, request):
        """Get all root categories (no parent)."""
        root_categories = self.queryset.filter(parent_category=None, is_active=True)
        serializer = CategorySerializer(root_categories, many=True)
        return Response(serializer.data)


class BrandViewSet(viewsets.ModelViewSet):
    """
    ViewSet for Brand CRUD operations.
    
    Endpoints:
    - GET /api/brands/ - List all brands
    - POST /api/brands/ - Create a new brand
    - GET /api/brands/{id}/ - Retrieve a brand
    - PUT /api/brands/{id}/ - Update a brand
    - PATCH /api/brands/{id}/ - Partial update a brand
    - DELETE /api/brands/{id}/ - Delete a brand
    - GET /api/brands/active/ - List active brands
    """
    
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['is_active']
    search_fields = ['name', 'description']
    ordering_fields = ['name', 'created_at']
    
    def get_serializer_class(self):
        """Return appropriate serializer based on action."""
        if self.action == 'list':
            return BrandListSerializer
        return BrandSerializer
    
    @action(detail=False, methods=['get'])
    def active(self, request):
        """Get all active brands."""
        active_brands = self.queryset.filter(is_active=True)
        serializer = BrandListSerializer(active_brands, many=True)
        return Response(serializer.data)
