from django.contrib import admin
from .models import Product, SalesSale, SalesProduct

# Register your models here.

admin.site.register(Product)
admin.site.register(SalesSale)
admin.site.register(SalesProduct)
