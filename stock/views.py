from rest_framework import viewsets
from .models import Product, TechnicalData
from .serializers import ProductSerializer, TechnicalDataSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class TechnicalDataViewSet(viewsets.ModelViewSet):
    queryset = TechnicalData.objects.all()
    serializer_class = TechnicalDataSerializer


