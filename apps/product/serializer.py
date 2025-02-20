from rest_framework import serializers
from apps.product.models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['id', 'title', 'description', 'price', 'is_active', 'created_at']