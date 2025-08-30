from django.db import models
from utilitie.models import DealerModel, EmployeeModel
# Create your models here.

class OrderModel(models.Model):
    customar_name = models.CharField(max_length=166)
    memo_number = models.CharField(max_length=20)
    cutomar_phone = models.CharField(max_length=20)
    product_name = models.CharField(max_length=266)
    details = models.TextField()
    product_image = models.ImageField(upload_to='product_image')
    delivery_address = models.TextField()
    total_price = models.FloatField(default=0)
    advance_payment = models.FloatField(default=0)
    delivery_date = models.DateField()
    frame_show_date = models.DateField()
    dealer = models.ForeignKey(DealerModel ,on_delete=models.DO_NOTHING)
    employee = models.ForeignKey(EmployeeModel ,on_delete=models.DO_NOTHING)
    order_status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return self.customar_name
    

    