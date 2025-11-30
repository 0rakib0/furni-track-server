from celery import shared_task
from django.utils import timezone
from order_management.models import OrderModel
import json
from django.utils.timezone import timedelta
from django.utils import timezone
from django.db.models import Q
# celery worker task list here.........


today = timezone.localdate() 
tomorrow = today + timedelta(days=1)
three_days = today + timedelta(days=3)


@shared_task
def celery_beat_test():
    print('Celery Beat Task executed!---1')
    return "Done"

@shared_task
def CreateOrderSheet():
    print('Celery Beat Task executed!---1')
    return "Done"

@shared_task(bind=True)
def GetFilterData(self, date):
    print("All Filter data in here")
    return "Done"


# all periodic task list here...........
@shared_task
def DeliveryOrderReminder():    
    orders = OrderModel.objects.select_related(
        "customar",
        "dealer",
        "employee"
    )
    
    todays_delivery_order = orders.filter(delivery_date=today)
    delivery_reminder = orders.filter(Q(delivery_date__range=(tomorrow, three_days)) & Q(order_status=False))
    
    print('Todays order list--------')
    return "Task Complated"

@shared_task
def FrameShowDateReminder():
    orders = OrderModel.objects.select_related(
        "customar",
        "dealer",
        "employee"
    )
    todays_frameshow_order = orders.filter(delivery_date=today)
    frameshow_reminder = orders.filter(Q(frame_show_date__range=(tomorrow, three_days)) & Q(order_status=False))
    print('All Frame Show Date Reminder here--------')
    return "Task Complated"

@shared_task
def DuePaymentReminder():
    orders = OrderModel.objects.select_related(
        "customar",
        "dealer",
        "employee"
    )
    todays_due_payment_client = orders.filter(next_advance_payment_date=today)
    print('all due payment customer reminder here--------')
    return "Task Complated"


@shared_task
def ServiceDateReminder():
    print("This all customar service list data here")
    return "Task Complated"