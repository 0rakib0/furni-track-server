from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from .models import OrderModel, CustomerModel
from .serializers import OrderSerializer, CustomarSerializer
from rest_framework.views import APIView
# Create your views here.


class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    queryset = OrderModel.objects.all()
    
class CustomarViewSet(viewsets.ModelViewSet):
    serializer_class = CustomarSerializer
    queryset = CustomerModel.objects.all()
    
    
class OrderManagementDashbord(APIView):
    def get(self, request):
        # get latest 10 data
        recent_order = OrderModel.objects.all().order_by('-id')[:10]
        recent_serializer = OrderSerializer(recent_order, many=True)
        
        # get only pending order data
        pending_order = OrderModel.objects.filter(order_status=False).order_by("-id")[:10]
        pending_serializer = OrderSerializer(pending_order, many=True)
        return Response({
            'recent_order':recent_serializer.data,
            'pending_order':pending_serializer.data
        })
    
    

