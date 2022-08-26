import pika 

class EventProducer(object): 
    def __init__(self, queue_name):
        """
        Conection to rabbbit     
        """
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host="rabbitmq"))
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue=queue_name, durable=True)
        
        self.channel.basic_publish(exchange="", routing_key="admin", body="hello", 
                          properties=pika.BasicProperties(delivery_mode=2))
        """
        channel.close()
        connection.close()
        """
    
    