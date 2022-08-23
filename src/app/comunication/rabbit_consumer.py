import pika 

# params = pika.URLParameters('amqp://user:bitnami@rabbitmq:5672//')

connection = pika.BlockingConnection(pika.ConnectionParameters(host="rabbitmq"))

channel = connection.channel()

channel.queue_declare(queue="admin")

def callback(ch, method, properties, body): 
    print("recived in admin")
    print(body)
    pass 

channel.basic_consume(queue="admin", on_message_callback=callback)

print("start consuming")

channel.start_consuming()

channel.close()