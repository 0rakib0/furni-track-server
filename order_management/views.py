from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from .models import OrderModel, CustomerModel
from .serializers import OrderSerializer, CustomarSerializer
from rest_framework.views import APIView
from django.db.models import Q
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
        upcomming_delivery = OrderModel.objects.filter(order_status=False).order_by("delivery_date")[:10]
        upcommingDeliverySerializer = OrderSerializer(upcomming_delivery, many=True)
        return Response({
            'recent_order':recent_serializer.data,
            'upcomming_delivery':upcommingDeliverySerializer.data
        })
    
class OrderSearch(APIView):
    def get(self, request):
        query = request.GET.get('order-search')
        if query:
            orders = OrderModel.objects.filter(Q( memo_number = query) | Q(customar__phone = query))
        else:
            orders = OrderModel.objects.all()

        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)
