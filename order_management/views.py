from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from .models import OrderModel, CustomerModel
from .serializers import OrderSerializer
# Create your views here.


class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    queryset = OrderModel.objects.all()
