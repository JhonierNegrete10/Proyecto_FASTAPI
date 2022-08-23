# from time import sleep
# from celery import Celery
# from celery.utils.log import get_task_logger
# import pika

# celery = Celery('worker', broker='amqp://user:bitnami@localhost:5672//')
# celery_log = get_task_logger(__name__)

# # Create Order - Run Asynchronously with celery
# # Example process of long running task
# @celery.task
# async def create_order(name, quantity):
    
# #     # 5 seconds per 1 order
#     complete_time_per_item = 5
    
#     # Keep increasing depending on item quantity being ordered
#     sleep(complete_time_per_item * quantity)
# # Display log    
#     celery_log.info(f"Order Complete!")
#     return {"message": f"Hi {name}, Your order has completed!",
#             "order_quantity": quantity}