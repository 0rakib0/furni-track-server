from celery import shared_task
from django.template.loader import render_to_string
from django.utils import timezone
from order_management.models import OrderModel
from .models import CustomarComplain
import json
from django.utils.timezone import timedelta
from django.utils import timezone
from django.db.models import Q
from .sendmail import SendMail
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
    delivery_reminder = orders.filter(
        Q(delivery_date__range=(tomorrow, three_days)) &
        Q(order_status=False)
    )
    
    if not todays_delivery_order or not delivery_reminder:
        return "No Order delivery for next 3 days"
    
    html_content = render_to_string(
        'emails_template/order_result.html',
        {
        "todays_delivery_order" : todays_delivery_order,
        'delivery_reminder':delivery_reminder
        }
    )
    subject = "Daily Delivery Report"
    SendMail(subject, html_content)
    return "Email successfully send"

@shared_task
def FrameShowDateReminder():
    orders = OrderModel.objects.select_related(
        "customar",
        "dealer",
        "employee"
    )
    
    todays_frameshow_order = orders.filter(delivery_date=today)
    frameshow_reminder = orders.filter(Q(frame_show_date__range=(tomorrow, three_days)) & Q(order_status=False))
    if not todays_frameshow_order or not frameshow_reminder:
        return "No frame date for next 3 days"
    
    html_content = render_to_string(
        'emails_template/frameshowreminder.html',
        {
        "todays_frameshow_order" : todays_frameshow_order,
        'frameshow_reminder':frameshow_reminder
        }
    )
    
    subject = "Daily Frame show Report"
    SendMail(subject, html_content)
    
    return "Task Complated"

@shared_task
def DuePaymentReminder():
    orders = OrderModel.objects.select_related(
        "customar",
        "dealer",
        "employee"
    )
    todays_due_payment_client = orders.filter(Q(next_advance_payment_date=today) & Q(order_status=False))
    
    if not todays_due_payment_client:
        return "No due payment date for any client today"
    
    html_content = render_to_string(
        'emails_template/duepaymendreminder.html.html',
        {
        "todays_due_payment_client" : todays_due_payment_client
        }
    )
    
    subject = "Due payment date reminder"
    SendMail(subject, html_content)
    return "Task Complated"


@shared_task
def ServiceDateReminder():
    complains = CustomarComplain.objects.filter(status=False)
    
    todays_service = complains.filter(service_date=today)
    service_reminder = complains.filter(service_date__range=(tomorrow, three_days))
    
    if not todays_service or not service_reminder:
        return "No service available today"
    
    html_content = render_to_string(
        'emails_template/service.html',
        {
        "todays_service" : todays_service,
        "service_reminder":service_reminder
        }
    )
    
    subject = "Today's service date reminder"
    SendMail(subject, html_content)
    return "Task Complated"