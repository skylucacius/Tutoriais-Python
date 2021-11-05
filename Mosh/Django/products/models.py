from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    stock = models.IntegerField()
    image_url = models.CharField(max_length=2084)

class Offer(models.Model):
    code = models.CharField(max_length=20)
    description = models.CharField(max_length=100)
    discount = models.FloatField()