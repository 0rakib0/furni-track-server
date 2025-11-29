from celery import shared_task
from django.utils import timezone
from order_management.models import OrderModel
import json


@shared_task
def celery_beat_test():
    print('Celery Beat Task executed!---1')
    return "Done"



@shared_task
def TodaysOrderTask():
    orders = OrderModel.objects.all()
    print(orders)
    print('Todays order list--------')
    return "Task Complated"