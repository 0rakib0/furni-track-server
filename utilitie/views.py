from django.shortcuts import get_object_or_404
from .serializers import DealerSerializer, EmployeeSerializer, DelaerPaymentSerializer, EmployeeExpenseSerializer
from .models import DealerModel, EmployeeModel, DelaerPayment, EmployeExpenses
from rest_framework import viewsets
from rest_framework.response import Response

# Create your views here.

class DealerViewSet(viewsets.ModelViewSet):
    serializer_class = DealerSerializer
    queryset = DealerModel.objects.all()
    
    
    
class DealerPaymentViewSet(viewsets.ModelViewSet):
    serializer_class = DelaerPaymentSerializer
    queryset = DelaerPayment.objects.all()
    
    
class EmployeeViewSet(viewsets.ModelViewSet):
    serializer_class = EmployeeSerializer
    queryset = EmployeeModel.objects.all()
    

class EmployeeExpenseViewSet(viewsets.ModelViewSet):
    serializer_class = EmployeeExpenseSerializer
    queryset = EmployeExpenses.objects.all()
    

