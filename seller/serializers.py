from rest_framework import serializers
from .models import Seller


class SellerSerializer(serializers.ModelSerializer):
    """Serializer for Seller model."""
    
    class Meta:
        model = Seller
        fields = '__all__'
        read_only_fields = ('joined_date', 'updated_at')


class SellerListSerializer(serializers.ModelSerializer):
    """Lightweight serializer for seller listings."""
    
    class Meta:
        model = Seller
        fields = ('id', 'seller_id', 'business_name', 'email', 'is_active', 'is_verified')


class SellerCreateUpdateSerializer(serializers.ModelSerializer):
    """Serializer for creating and updating sellers."""
    
    class Meta:
        model = Seller
        fields = '__all__'
        read_only_fields = ('joined_date', 'updated_at')
    
    def validate_gstin(self, value):
        """Validate GSTIN format (15 characters)."""
        if len(value) != 15:
            raise serializers.ValidationError("GSTIN must be exactly 15 characters.")
        return value.upper()
    
    def validate_pan(self, value):
        """Validate PAN format (10 characters)."""
        if len(value) != 10:
            raise serializers.ValidationError("PAN must be exactly 10 characters.")
        return value.upper()
    
    def validate_bank_ifsc(self, value):
        """Validate IFSC format (11 characters)."""
        if len(value) != 11:
            raise serializers.ValidationError("IFSC code must be exactly 11 characters.")
        return value.upper()
