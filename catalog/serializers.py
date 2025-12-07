from rest_framework import serializers
from .models import Category, Brand


class CategorySerializer(serializers.ModelSerializer):
    """Serializer for Category model."""
    
    subcategories = serializers.SerializerMethodField()
    
    class Meta:
        model = Category
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')
    
    def get_subcategories(self, obj):
        """Get immediate subcategories."""
        subcats = obj.subcategories.filter(is_active=True)
        return CategoryListSerializer(subcats, many=True).data


class CategoryListSerializer(serializers.ModelSerializer):
    """Lightweight serializer for category listings."""
    
    class Meta:
        model = Category
        fields = ('id', 'name', 'is_active', 'display_order')


class BrandSerializer(serializers.ModelSerializer):
    """Serializer for Brand model."""
    
    class Meta:
        model = Brand
        fields = '__all__'
        read_only_fields = ('created_at',)


class BrandListSerializer(serializers.ModelSerializer):
    """Lightweight serializer for brand listings."""
    
    class Meta:
        model = Brand
        fields = ('id', 'name', 'is_active')
