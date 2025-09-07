from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'orders', views.OrderViewSet, basename='orders')
router.register(r'customars', views.CustomarViewSet, basename='customar')
urlpatterns = router.urls


urlpatterns = [
    path('order-management/', views.OrderManagementDashbord.as_view()),
    path('order-search/', views.OrderSearch.as_view()),
    path('recent-delivery-order/', views.RecentDeliveryData, name='recent_delivery'),
    path('', include(router.urls)),
]

