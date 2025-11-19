from django.shortcuts import get_object_or_404
from .serializers import DealerSerializer, EmployeeSerializer, DelaerPaymentSerializer, EmployeeExpenseSerializer, ComplainSerializer
from .models import DealerModel, EmployeeModel, DelaerPayment, EmployeExpenses, CustomarComplain
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

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
    

