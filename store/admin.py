from django.contrib import admin

from .models import Customer,Products,Order,OrderItem,ShippingAddress

admin.site.register(Customer)
admin.site.register(Products)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)


# Register your models here.
