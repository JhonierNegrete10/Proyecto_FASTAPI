import pika 

class EventProducer(object): 
    def __init__(self, queue_name= "created", 
                #  body= "hello"
                 ):
        """
        Conection to rabbbit     
        """
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host="rabbitmq"))
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue=queue_name, 
                                   durable=True
                                   )
        
        # self.channel.basic_publish(exchange="user", routing_key="created", body=body, 
        #                   properties=pika.BasicProperties(delivery_mode=2))
        
    def close(self): 
        self.channel.close()
        self.connection.close()
        """
        """
    
    def send_body(self, exchange="", routing_key= "created", body= "hello"):
        
        self.channel.basic_publish(exchange=exchange, 
                                   routing_key=routing_key, 
                                   body=body, 
                                    properties=pika.BasicProperties(
                                        delivery_mode=2, 
                                        content_type= "aplication/json"
                                        ))
        
        self.close()
        
