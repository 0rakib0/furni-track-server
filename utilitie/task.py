from celery import shared_task
from time import sleep

@shared_task
def test_celery_func():
    for i in range(20):
        print("Current Number: ", i)
        sleep(1)
    return "test task successfully complated!"


@shared_task
def celery_beat_test():
    print('Celery Beat Task executed!')
    return "Done"

