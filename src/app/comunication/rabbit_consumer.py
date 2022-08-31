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
        self.channel.queue_declare(queue=self.queue_name, 
                                   durable=True)
        self.channel.basic_qos(prefetch_count=1)
        
        
    def close(self): 
        self.channel.stop_consuming()
        self.connection.close()
        
        
    def callback(self, ch, method, properties, body): 
        print("recived in admin")
        ch.basic_ack(delivery_tag = method.delivery_tag)
        return body 
        # ch.basic_ack(delivery_tag=method.delivery_tag)
    
    
    def consume(self, ):
        # to make sure the consumer receives only one message at a time
        # next message is received only after acking the previous one
        # 
        # channel.basic_qos(prefetch_count=1)
        #  
        self.channel.basic_consume(queue=self.queue_name,
                              on_message_callback=self.callback, 
                            #   auto_ack=True
                              )
        data = self.channel.start_consuming()
        # self.close()
        return data 
        # self.channel.close()
    
    
    def consume_user_created(self, ):
        # to make sure the consumer receives only one message at a time
        # next message is received only after acking the previous one
        # 
        # channel.basic_qos(prefetch_count=1)
        #  
        self.channel.basic_consume(queue=self.queue_name,
                              on_message_callback=self.callback, 
                            #   auto_ack=True
                              )
        data = self.channel.start_consuming()
        self.close()
        return data 
        # self.channel.close()
        
    def get_queue(self): 
        method_frame, header_frame, body = self.channel.basic_get(self.queue_name)
        print(method_frame, header_frame, body)
        if method_frame:
            self.channel.basic_ack(method_frame.delivery_tag)
        # self.channel.basic_get()
        return body
