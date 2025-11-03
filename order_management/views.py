from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from .models import OrderModel, CustomerModel
from .serializers import OrderSerializer, CustomarSerializer
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from django.utils.timezone import timedelta
from django.utils import timezone
from rest_framework import status
from django.db.models import Q, F
from django.db.models.functions import TruncDate
from django.db.models import Count
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
    

class DeliveredOrder(APIView):
    def get(self, request):
        orders = OrderModel.objects.filter(Q( order_status = True))
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)

class OrderSearch(APIView):
    def get(self, request):
        query = request.GET.get('order-search', '')
        if query:
            orders = OrderModel.objects.filter(Q( memo_number = query) | Q(customar__phone = query))
        else:
            orders = OrderModel.objects.all()

        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)
    
@api_view(["GET"])
def RecentDeliveryData(request):
    try:
        today = timezone.localdate() 
        tomorrow = today + timedelta(days=1)
        three_days = today + timedelta(days=3)
        
        todays_delivery_order = OrderModel.objects.filter(Q(delivery_date=today))
        today_order_serializer = OrderSerializer(todays_delivery_order, many=True)
        
        tomorrow_delivery_order = OrderModel.objects.filter(Q(delivery_date=tomorrow))
        tommorow_order_serializer = OrderSerializer(tomorrow_delivery_order, many=True)
        
        after_three_days_delivery_order = OrderModel.objects.filter(delivery_date__range=(today,three_days))
        after_three_days_order_serializer = OrderSerializer(after_three_days_delivery_order, many=True)
        return Response({
            'todays_delivery':today_order_serializer.data,
            "tomorrow_delivery_orders":tommorow_order_serializer.data,
            "after_three_days_delivery_order":after_three_days_order_serializer.data
            }, status=status.HTTP_200_OK)
    except Exception as e:
        return Response(
            {'error':str(e)},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )
        
        
@api_view(['GET'])
def ChartData(request):
    try:
        order_data = (
            OrderModel.objects
            .annotate(date=TruncDate("created_at"))
            .values('date')
            .annotate(count=Count('id'))
            .order_by('date')
        )
        
        # ontime_delivery_data = (
        #     OrderModel.objects
        #     .filter(order_status=True, delivery_date=F('delivery_date'))
        #     .annotate(date=TruncDate("delivery_date"))
        #     .values("date")
        #     .annotate(count=Count("id"))
        #     .order_by("date")
        # )
        return Response({'order_data':order_data}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response ({"error":str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

