from django.db import models

# Create your models here.

class DealerModel(models.Model):
    name = models.CharField(max_length=166)
    age = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    address = models.TextField()
    dealer_image = models.ImageField(upload_to='dealer_image')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return self.name
    
    
    
class EmployeeModel(models.Model):
    name = models.CharField(max_length=166)
    age = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    position = models.CharField(max_length=40)
    join_date = models.DateField()
    performance_status = models.CharField(max_length=30)
    address = models.TextField()
    employee_image = models.ImageField(upload_to='dealer_image')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return self.name