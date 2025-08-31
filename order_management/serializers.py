from rest_framework import serializers
from .models import OrderModel, CustomerModel

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderModel
        fields = '__all__'
        
class CustomarSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerModel
        fields = '__all__'
  
  