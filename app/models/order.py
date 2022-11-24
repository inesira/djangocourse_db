from django.db import models
from app.models import Category,Customer

class Order(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity = models.CharField(max_length=45)
    total = models.CharField(max_length=45)
