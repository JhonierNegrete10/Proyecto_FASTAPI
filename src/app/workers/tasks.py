from time import sleep
from celery import Celery
from celery.utils.log import get_task_logger
# import pika
from comunication.rabbit_init  import EventProducer
from workers.celery import app, celery_log

"""
the app.task will be execute by the Celery Worker
"""
# # Create Order - Run Asynchronously with celery
# # Example process of long running task
@app.task(bin = True)
def create_order(name, quantity):
    
#     # 5 seconds per 1 order
    complete_time_per_item = 5
    # publish()
    # Keep increasing depending on item quantity being ordered
    sleep(complete_time_per_item * quantity)
# Display log    
    celery_log.info(f"Order Complete!")
    print("_"*20)
    EventProducer("admin")
    print("working")
    return {"message": f"Hi {name}, Your order has completed!",
            "order_quantity": quantity}