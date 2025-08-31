from django.contrib import admin
from .models import OrderModel, CustomerModel


# Register your models here.
admin.site.register(OrderModel)
admin.site.register(CustomerModel)
