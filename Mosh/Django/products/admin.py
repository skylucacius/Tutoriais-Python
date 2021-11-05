from products.models import Product
from django.contrib import admin
from django.db import models
# Register your models here.
class ProductAdmin(models.Model):
    list = ()

admin.site.register(Product, ProductAdmin)