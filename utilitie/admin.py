from django.contrib import admin
from .models import DealerModel, EmployeeModel
# Register your models here.
admin.site.register(DealerModel)
admin.site.register(EmployeeModel)