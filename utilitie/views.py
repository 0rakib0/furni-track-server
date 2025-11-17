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
    def get(self, request):
        try:
            # here need to apply filter with paramiters
            complain_data = CustomarComplain.objects.all()
            seriaizer = ComplainSerializer(complain_data, many=True)
            return Response(seriaizer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(
                {'error':str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
        return Response({'message':'Customar complain data comming....'})
    

