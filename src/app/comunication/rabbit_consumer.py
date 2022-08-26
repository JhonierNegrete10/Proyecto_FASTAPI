import pika 

# params = pika.URLParameters('amqp://user:bitnami@rabbitmq:5672//')

class EventConsumer(object): 
    def __init__(self, queue_name):
        """
        Conection to rabbbit     
        """
        self.queue_name = queue_name
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host="rabbitmq"))
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue=self.queue_name)
        
        
    def callback(self, ch, method, properties, body): 
        print("recived in admin")
        print(body)
        # ch.basic_ack(delivery_tag=method.delivery_tag)
    
    
    def consume(self, ):
        # to make sure the consumer receives only one message at a time
        # next message is received only after acking the previous one
        # 
        # channel.basic_qos(prefetch_count=1)
        #  
        self.channel.basic_consume(queue=self.queue_name,
                              on_message_callback=self.callback, 
                              auto_ack=True)
        self.channel.start_consuming()
        self.channel.close()
