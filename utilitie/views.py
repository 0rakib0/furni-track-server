from django.shortcuts import get_object_or_404
from .serializers import DealerSerializer
from .models import DealerModel
from rest_framework import viewsets
from rest_framework.response import Response

# Create your views here.

class DealerViewSet(viewsets.ModelViewSet):
    serializer_class = DealerSerializer
    queryset = DealerModel.objects.all()
