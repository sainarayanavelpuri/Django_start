
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length = 256)
    price = models.IntegerField(default = 1)
    stock = models.IntegerField(default = 0)
    image_url = models.URLField(max_length = 500, null = True)

    def __repr__(self):
        return f'{self.name} cost of {self.price} Rupees Only and stock left {self.stock} only {self.image_url}'
    def __str__(self):
        return f'{self.name} cost of {self.price} Rupees Only and stock left {self.stock} only {self.image_url}'


    