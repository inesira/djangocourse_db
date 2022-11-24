from django.db import models

class Customer(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    tel = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    adress = models.CharField(max_length=45)

    