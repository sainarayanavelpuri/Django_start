
from django.db import models
class Product(models.Model):
    product_name = models.CharField(max_length = 256)
    product_price = models.IntegerField(default = 0)
    product_stock = models.IntegerField(default = 0)
    product_imageurls= models.CharField(max_length=256, null = True)
    def __repr__(self):
        return f'{self.product_name} price is {self.product_price} & stock available is {self.product_stock} <br> {self.product_imageurls}'                           
    def __str__(self):
        return f'{self.product_name} price is {self.product_price} & stock available is {self.product_stock} <br> {self.product_imageurls}'
class cart (models.Model):
    Product = models.ForeignKey(Product, on_delete = models.CASCADE)
    date = models.DateTimeField('date')
    is_present = models.BooleanField()


    