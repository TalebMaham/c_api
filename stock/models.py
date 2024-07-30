from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name

class TechnicalData(models.Model):
    message = models.CharField(max_length=255)
    value = models.CharField(max_length=255)
    value_type = models.CharField(max_length=50)
    product = models.ForeignKey(Product, related_name='technical_data', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.product.name} - {self.message}"


