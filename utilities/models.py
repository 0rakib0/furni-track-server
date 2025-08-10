from django.db import models

# Create your models here.

class DealerModel(models.Model):
    name = models.CharField(max_length=166)
    age = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    address = models.TextField()
    dealer_image = models.ImageField(upload_to='dealer_image')
    
    
    def __str__(self):
        return self.name