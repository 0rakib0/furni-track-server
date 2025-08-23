from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views

urlpatterns = [
]



router = DefaultRouter()
router.register(r'dealers', views.DealerViewSet, basename='dealer')
router.register(r'employee', views.EmployeeViewSet, basename='employee')
urlpatterns = router.urls


