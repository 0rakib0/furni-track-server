from django.db import models
from utilities.models import DealerModel
# Create your models here.

class OrderModel(models.Model):
    customar_name = models.CharField(max_length=166)
    memo_number = models.CharField(max_length=20)
    cutomar_phone = models.CharField(max_length=20)
    delivery_address = models.TextField()
    delivery_date = models.DateField()
    frame_show_date = models.DateField()
    dealer = models.ForeignKey(on_delete=models.DO_NOTHING)
    