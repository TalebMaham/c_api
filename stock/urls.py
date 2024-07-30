from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, TechnicalDataViewSet

router = DefaultRouter()
router.register(r'products', ProductViewSet, basename='product')
router.register(r'technical_data', TechnicalDataViewSet, basename='technical_data')

urlpatterns = [
    path('', include(router.urls)),
]
