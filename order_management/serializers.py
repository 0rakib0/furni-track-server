from rest_framework import serializers
from .models import OrderModel, CustomerModel
from utilitie.serializers import DealerSerializer, EmployeeSerializer

class CustomarSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerModel
        fields = '__all__'
  
class OrderSerializer(serializers.ModelSerializer):
    customar = CustomarSerializer(read_only=True)
    dealer = DealerSerializer(read_only=True)
    employee = EmployeeSerializer(read_only=True)
    class Meta:
        model = OrderModel
        fields = '__all__'
        

  