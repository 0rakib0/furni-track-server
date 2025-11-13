from rest_framework import serializers
from .models import DealerModel, DelaerPayment, EmployeeModel, EmployeExpenses

class DealerSerializer(serializers.ModelSerializer):
    class Meta:
        model = DealerModel
        fields = '__all__'
        
class DelaerPaymentSerializer(serializers.ModelSerializer):
    dealer = DealerSerializer(read_only=True)
    
    dealer_id = serializers.PrimaryKeyRelatedField(
        queryset=DealerModel.objects.all(), source='dealer', write_only=True
    )
    class Meta:
        model = DelaerPayment
        fields = '__all__'
        
        
class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model=EmployeeModel
        fields = '__all__'
        
        
class EmployeeExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model=EmployeExpenses
        fields = '__all__'