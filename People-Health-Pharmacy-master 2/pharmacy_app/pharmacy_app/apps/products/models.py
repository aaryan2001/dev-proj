import datetime
from django.db import models

from django.utils import timezone
# Create your models here.


class Product(models.Model):
    product_name = models.CharField('Product Name', max_length=50)
    product_price = models.FloatField('Product Price')
    remaining_stock = models.IntegerField('Remaining Stock')
    initial_stock = models.IntegerField('Initial Stock')

    def __str__(self):
        return self.product_name


class SalesSale(models.Model):
    sales_id = models.IntegerField('Sale ID', default=0)
    total = models.FloatField('Total Amount')

    def __str__(self):
        return "Sale ID: " + self.sales_id.__str__()


class SalesProduct(models.Model):
    sales_id = models.IntegerField('Sale ID', default=0)
    product_name = models.CharField('Product Name', max_length=50)
    product_quantity = models.IntegerField('Quantity Ordered')
    total = models.FloatField('Total Amount for Item(s)')

    def __str__(self):
        return "Sale ID: " + self.sales_id.__str__() + " - " + self.product_name

    def product_price(self):
        return self.total / self.product_quantity
