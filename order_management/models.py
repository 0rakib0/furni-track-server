from django.db import models
from utilitie.models import DealerModel, EmployeeModel
# Create your models here.


class CustomerModel(models.Model):
    name = models.CharField(max_length=166)
    phone = models.CharField(max_length=20, unique=True)
    email = models.EmailField(null=True, blank=True)
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.phone})"



class OrderModel(models.Model):
    customar = models.ForeignKey(CustomerModel ,on_delete=models.DO_NOTHING)
    memo_number = models.CharField(max_length=20)
    product_name = models.CharField(max_length=266)
    details = models.TextField()
    product_image = models.ImageField(upload_to='product_image')
    delivery_address = models.TextField()
    total_price = models.FloatField(default=0)
    advance_payment = models.FloatField(default=0)
    delivery_date = models.DateField()
    initial_dalivery_date = models.DateField()
    next_advance_payment_date = models.DateField(null=True, blank=True)
    frame_show_date = models.DateField()
    
    dealer = models.ForeignKey(DealerModel ,on_delete=models.DO_NOTHING)
    employee = models.ForeignKey(EmployeeModel ,on_delete=models.DO_NOTHING)
    
    order_status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return self.customar.name
    

    