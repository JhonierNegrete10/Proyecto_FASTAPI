
from celery import Celery
from celery.utils.log import get_task_logger

# from comunication.rabbit_init  import publish
# celery = Celery('worker', broker='amqp://user:bitnami@localhost:5672//')

app = Celery('workers',
    broker='amqp://guest:guest@rabbitmq:5672//', 
     backend='rpc://',
    include=['workers.tasks']
)
app
celery_log = get_task_logger(__name__)

if __name__ =="__main__": 
    app.start()



"""
@app.task(bind=True, default_retry_delay=300, max_retries=5)
def my_task_A():
    try:
        print("doing stuff here...")
    except SomeNetworkException as e:
        print("maybe do some clenup here....")
        self.retry(e)
        
        
@shared_task(bind=True,autoretry_for=(Exception,), retry_backoff=True, retry_kwargs={"max_retries": 5},
             name='universities:get_all_universities_task')
             

app.conf.task_default_queue = ‘default’
app.conf.tasks_queues 
CELERY_QUEUES = (
    Queue('default', Exchange('default'), routing_key='default'),
    Queue('for_task_A', Exchange('for_task_A'), routing_key='for_task_A'),
    Queue('for_task_B', Exchange('for_task_B'), routing_key='for_task_B'),
)

CELERY_ROUTES = {
    'my_taskA': {'queue': 'for_task_A', 'routing_key': 'for_task_A'},
    'my_taskB': {'queue': 'for_task_B', 'routing_key': 'for_task_B'},
}


-----------example docs 
from kombu import Exchange, Queue

task_queues = (
    Queue('celery', routing_key='celery'),
    Queue('transient', Exchange('transient', delivery_mode=1),
          routing_key='transient', durable=False),
)
task_routes = {
    'proj.tasks.add': {'queue': 'celery', 'delivery_mode': 'transient'}
}
task.apply_async(args, queue='transient')
----------- 

retry_limit 
autoretry_for 
retry_backoff 


from celery.exceptions import SoftTimeLimitExceeded

@app.task(task_time_limit=60, task_soft_time_limit=45)
def my_task():
    try:
        something_possibly_long()
    except SoftTimeLimitExceeded:
        recover()
        
        
        def get_task_info(task_id):
    #
    # return task info according to the task_id
    #
    task = AsyncResult(task_id)
    if task.state == "FAILURE":
        error = str(task.result)
        response = {
            "state": task.state,
            "error": error,
        }
    else:
        response = {
            "state": task.state,
        }
    return response
"""