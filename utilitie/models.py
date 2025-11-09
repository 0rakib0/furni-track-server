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
    email = models.EmailField(unique=True, null=True, blank=True)
    company_name = models.CharField(max_length=255, null=True, blank=True)
    nid_number = models.CharField(max_length=30, null=True, blank=True) 
    trade_license = models.CharField(max_length=50, null=True, blank=True)
    total_deals = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True) 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return self.name
    

class DelaerPayment(models.Model):
    dealer = models.ForeignKey(DealerModel, on_delete=models.DO_NOTHING)
    ref_memo = models.CharField(max_length=20, blank=True, null=True)
    payment_method = models.CharField(max_length=166)
    amount = models.IntegerField(default=0)
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
    email = models.EmailField(unique=True, null=True, blank=True)
    salary = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    national_id = models.CharField(max_length=30, null=True, blank=True)  # NID/Passport No
    emergency_contact = models.CharField(max_length=20, null=True, blank=True)
    department = models.CharField(max_length=50, null=True, blank=True)  # যেমন: Sales, Delivery, Factory
    is_active = models.BooleanField(default=True)  # চাকরিতে আছে কিনা
    leave_days = models.PositiveIntegerField(default=0)  # মোট ছুটির সংখ্যা
    notes = models.TextField(null=True, blank=True)  # Extra remark/performance notes
    address = models.TextField()
    employee_image = models.ImageField(upload_to='dealer_image')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return self.name