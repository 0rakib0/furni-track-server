from rest_framework import serializers
from .models import DealerModel, EmployeeModel

class DealerSerializer(serializers.ModelSerializer):
    class Meta:
        model = DealerModel
        fields = '__all__'
        
        
class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model=EmployeeModel
        fields = '__all__'