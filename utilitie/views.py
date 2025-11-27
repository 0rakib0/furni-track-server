from django.shortcuts import get_object_or_404
from .serializers import DealerSerializer, EmployeeSerializer, DelaerPaymentSerializer, EmployeeExpenseSerializer, ComplainSerializer
from .models import DealerModel, EmployeeModel, DelaerPayment, EmployeExpenses, CustomarComplain
from order_management.models import OrderModel, CustomerModel
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from django.utils import timezone
from order_management.serializers import OrderSerializer
from django.db.models import Q, F
from .task import test_celery_func


# Create your views here.

class DealerViewSet(viewsets.ModelViewSet):
    serializer_class = DealerSerializer
    queryset = DealerModel.objects.all()
    
    
    
class DealerPaymentViewSet(viewsets.ModelViewSet):
    serializer_class = DelaerPaymentSerializer
    queryset = DelaerPayment.objects.all()
    
    
class EmployeeViewSet(viewsets.ModelViewSet):
    serializer_class = EmployeeSerializer
    queryset = EmployeeModel.objects.all()
    

class EmployeeExpenseViewSet(viewsets.ModelViewSet):
    serializer_class = EmployeeExpenseSerializer
    queryset = EmployeExpenses.objects.all()


class CustomarComplainView(APIView):
    def post(self, request, format=None):
        complain_data = ComplainSerializer(data=request.data)
        if complain_data.is_valid():
            complain_data.save()
            return Response(complain_data.data, status=status.HTTP_201_CREATED)
        return Response(
            complain_data.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
    def get(self, request):
        query_data = request.query_params.get('filter')

        filter_map = {
            'all-data': CustomarComplain.objects.all(),
            'pending-data': CustomarComplain.objects.filter(status=False),
            'complate-data': CustomarComplain.objects.filter(status=True),
        }

    # Default → all-data
        queryset = filter_map.get(query_data, filter_map['all-data']).order_by('-id')

        serializer = ComplainSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def delete(self, request, id):
        try:
            complain = CustomarComplain.objects.get(id=id)
        except CustomarComplain.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        complain.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def patch (self, request, id):
        print("--------Hello from Patch-------")
        try:
            complain = CustomarComplain.objects.get(id=id)
        except CustomarComplain.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        complain.status = True
        complain.save()
        return Response({"message": "Complain marked as completed"}, status=status.HTTP_200_OK)
        
    
@api_view(['GET'])
def dashbord(request):
    today = timezone.localdate() 
    tomorrow = today + timezone.timedelta(days=1)
    three_days = today + timezone.timedelta(days=3)
    # orders = OrderModel.objects.all()
    orders = OrderModel.objects.select_related(
        "customar",
        "dealer",
        "employee"
    )
    
    todays_delivery_order = orders.filter(delivery_date=today)
    today_order_serializer = OrderSerializer(todays_delivery_order, many=True)
    
    tomorrow_delivery_order = orders.filter(delivery_date=tomorrow)
    tomorrow_order_serializer = OrderSerializer(tomorrow_delivery_order, many=True)
    
    after_three_days_delivery_order = orders.filter(
        delivery_date__gt=today,
        delivery_date__lte=three_days
    )
    after_three_days_order_serializer = OrderSerializer(after_three_days_delivery_order, many=True)
    
    todays_orders = orders.filter(created_at__date=today)
    todays_order_serializer = OrderSerializer(todays_orders, many=True)
    
    data = {
        "total_order" : orders.count(),
        "pending_orders":orders.filter(order_status=False).count(),
        "total_customar": CustomerModel.objects.count(),
        "todays_orders" : todays_order_serializer.data,
        "todays_delivery_order":today_order_serializer.data,
        "tomorrow_delivery_order":tomorrow_order_serializer.data,
        "After3days_delivery_order":after_three_days_order_serializer.data
    }
    
    return Response(data)



@api_view(['GET'])
def test_celery(request):
    result = test_celery_func.delay()
    print(result)
    return Response({"Message":"task test rout successfully work!"})