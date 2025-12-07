from rest_framework import serializers
from .models import Order, OrderItem


class OrderItemSerializer(serializers.ModelSerializer):
    """Serializer for OrderItem model."""
    
    class Meta:
        model = OrderItem
        fields = '__all__'
        read_only_fields = ('id',)


class OrderSerializer(serializers.ModelSerializer):
    """Serializer for Order model with nested items."""
    
    items = OrderItemSerializer(many=True, read_only=True)
    
    class Meta:
        model = Order
        fields = '__all__'
        read_only_fields = ('order_date', 'updated_at')


class OrderListSerializer(serializers.ModelSerializer):
    """Lightweight serializer for order listings."""
    
    items_count = serializers.SerializerMethodField()
    
    class Meta:
        model = Order
        fields = ('id', 'order_id', 'customer_name', 'total_amount', 'status', 'order_date', 'items_count')
    
    def get_items_count(self, obj):
        return obj.items.count()


class OrderStatusUpdateSerializer(serializers.ModelSerializer):
    """Serializer for updating order status."""
    
    class Meta:
        model = Order
        fields = ('status',)
    
    def validate_status(self, value):
        """Validate status transitions."""
        valid_statuses = ['pending', 'confirmed', 'processing', 'shipped', 'delivered', 'cancelled', 'returned']
        if value not in valid_statuses:
            raise serializers.ValidationError(f"Status must be one of: {', '.join(valid_statuses)}")
        return value
