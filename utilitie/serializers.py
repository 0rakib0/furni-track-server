from rest_framework import serializers
from .models import DealerModel

class DealerSerializer(serializers.ModelSerializer):
    class Meta:
        model = DealerModel
        fields = '__all__'