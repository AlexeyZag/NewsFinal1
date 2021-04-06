from celery import shared_task
import time

@shared_task
def hello():
    print("Hello, world!")
    time.sleep(10)
