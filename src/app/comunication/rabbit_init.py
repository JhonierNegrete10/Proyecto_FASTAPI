import pika 

# params = pika.URLParameters('pyamqp://user:bitnami@rabbitmq:5672//')

connection = pika.BlockingConnection(pika.ConnectionParameters(host="rabbitmq"))

channel = connection.channel()

def publish(): 
    channel.basic_publish(exchange="", routing_key="admin", body="hello")
     