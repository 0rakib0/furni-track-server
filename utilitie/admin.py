from django.contrib import admin
from .models import DealerModel, EmployeeModel, DelaerPayment, EmployeExpenses, CustomarComplain
# Register your models here.
admin.site.register(DealerModel)
admin.site.register(DelaerPayment)
admin.site.register(EmployeeModel)
admin.site.register(EmployeExpenses)
admin.site.register(CustomarComplain)