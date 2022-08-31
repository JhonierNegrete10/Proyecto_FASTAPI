from time import sleep
from typing import Dict
from celery import Celery
from celery.utils.log import get_task_logger
# import pika
from comunication.rabbit_init  import EventProducer
from comunication.rabbit_consumer  import EventConsumer 
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
    rabbit = EventProducer()
    rabbit.send_body()
    print("working")
    return {"message": f"Hi {name}, Your order has completed!",
            "order_quantity": quantity}
    
    
@app.task(bin = True)
def publish_user_created_task(data: Dict): 
    celery_log.info(f"Order Complete!")
    rabbit= EventProducer()
    rabbit.send_body(body=data)
    return {"result": data}
    # return 
    
    
@app.task(bin=True)
def receive_user_published_task(): 
    celery_log.info(f"Order Complete!")
    rabbit = EventConsumer(queue_name="created")
    data = rabbit.consume()
    print(data)
    return  data


@app.task(bin=True)
def receive_user_task(): 
    celery_log.info(f"Order Complete!")
    rabbit = EventConsumer(queue_name="created")
    data = rabbit.get_queue()
    print(data)
    return data
    

@app.task(bin=True)
def init_consume(): 
    celery_log.info(f"Order Complete!")
    rabbit = EventConsumer(queue_name="created")
    data = rabbit.consume()
    # return data 
