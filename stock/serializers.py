from rest_framework import serializers
from .models import Product, TechnicalData

class TechnicalDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = TechnicalData
        fields = ['id', 'message', 'value', 'value_type', 'product']

class ProductSerializer(serializers.ModelSerializer):
    technical_data = TechnicalDataSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'technical_data']
