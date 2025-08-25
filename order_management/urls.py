from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter
from . import views



urlpatterns = [
    
]

router = DefaultRouter()
router.register(r'orders', views.OrderViewSet, basename='orders')
urlpatterns = router.urls