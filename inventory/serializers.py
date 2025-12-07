from rest_framework import serializers
from .models import Inventory


class InventorySerializer(serializers.ModelSerializer):
    """Serializer for Inventory model."""
    
    is_low_stock = serializers.BooleanField(read_only=True)
    
    class Meta:
        model = Inventory
        fields = '__all__'
        read_only_fields = ('updated_at',)


class InventoryUpdateSerializer(serializers.ModelSerializer):
    """Serializer for updating inventory quantities."""
    
    class Meta:
        model = Inventory
        fields = ('available_quantity', 'reserved_quantity', 'warehouse_location', 'last_restocked')
    
    def validate_available_quantity(self, value):
        """Ensure available quantity is non-negative."""
        if value < 0:
            raise serializers.ValidationError("Available quantity cannot be negative.")
        return value
    
    def validate_reserved_quantity(self, value):
        """Ensure reserved quantity is non-negative."""
        if value < 0:
            raise serializers.ValidationError("Reserved quantity cannot be negative.")
        return value


class InventoryListSerializer(serializers.ModelSerializer):
    """Lightweight serializer for inventory listings."""
    
    is_low_stock = serializers.BooleanField(read_only=True)
    
    class Meta:
        model = Inventory
        fields = ('id', 'product_sku', 'product_name', 'available_quantity', 'is_low_stock')
