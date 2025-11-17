from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views



router = DefaultRouter()
router.register(r'dealers', views.DealerViewSet, basename='dealer')
router.register(r'employee', views.EmployeeViewSet, basename='employee')
router.register(r'dealer-payment', views.DealerPaymentViewSet, basename='dealer_payment')
router.register(r'employee-expense', views.EmployeeExpenseViewSet, basename='employee_expense')
urlpatterns = router.urls


urlpatterns = [
    path('customar-complain/', views.CustomarComplainView.as_view()),
    path('', include(router.urls)),
]




