import os
from celery import Celery
from celery.schedules import crontab

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'furnitrack_server.settings')

app = Celery('furnitrack_server')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()


app.conf.beat_schedule = {
    'todays_delivery_orders':{
        'task':'utilitie.tasks.DeliveryOrderReminder',
        'schedule':crontab(hour=0, minute=5),
    },
    'service_date_reminder':{
        'task':'utilitie.tasks.ServiceDateReminder',
        'schedule':crontab(hour=0, minute=10),
    }, 
    'frame_show_date_reminder':{
        'task':'utilitie.tasks.FrameShowDateReminder',
        'schedule':crontab(hour=0, minute=15),
    }, 
    'due_payment_reminder':{
        'task':'utilitie.tasks.DuePaymentReminder',
        'schedule':crontab(hour=0, minute=20),
    }
}
