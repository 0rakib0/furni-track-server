from rest_framework import serializers
from .models import OrderModel, CustomerModel
from utilitie.models import DealerModel, EmployeeModel
from utilitie.serializers import DealerSerializer, EmployeeSerializer

class CustomarSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerModel
        fields = '__all__'
  
class OrderSerializer(serializers.ModelSerializer):
    customar = CustomarSerializer(read_only=True)
    dealer = DealerSerializer(read_only=True)
    employee = EmployeeSerializer(read_only=True)
    
    customar_id = serializers.PrimaryKeyRelatedField(
        queryset=CustomerModel.objects.all(), source='customar', write_only=True
    )
    dealer_id = serializers.PrimaryKeyRelatedField(
        queryset=DealerModel.objects.all(), source='dealer', write_only=True
    )
    employee_id = serializers.PrimaryKeyRelatedField(
        queryset=EmployeeModel.objects.all(), source='employee', write_only=True
    )
    
    
    class Meta:
        model = OrderModel
        fields = '__all__'
        

  