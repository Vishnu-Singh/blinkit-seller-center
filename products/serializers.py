from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    """Serializer for Product model."""
    
    class Meta:
        model = Product
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')


class ProductListSerializer(serializers.ModelSerializer):
    """Lightweight serializer for product listings."""
    
    class Meta:
        model = Product
        fields = ('id', 'name', 'sku', 'price', 'status', 'category')


class ProductCreateUpdateSerializer(serializers.ModelSerializer):
    """Serializer for creating and updating products."""
    
    class Meta:
        model = Product
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')
    
    def validate_sku(self, value):
        """Ensure SKU is uppercase and unique."""
        return value.upper()
    
    def validate_price(self, value):
        """Ensure price is positive."""
        if value <= 0:
            raise serializers.ValidationError("Price must be greater than zero.")
        return value
    
    def validate_mrp(self, value):
        """Ensure MRP is positive."""
        if value <= 0:
            raise serializers.ValidationError("MRP must be greater than zero.")
        return value
