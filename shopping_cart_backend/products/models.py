from django.db import models

class Product(models.Model):
  productname = models.CharField(max_length=255)
  price = models.DecimalField(max_digits=10, decimal_places=2)