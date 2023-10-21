"""
Will send a message to RabbitMQ
"""
import pika

credentials = pika.PlainCredentials("guest", "guest")
connection = pika.BlockingConnection(pika.ConnectionParameters("localhost", credentials=credentials))
channel = connection.channel()

channel.queue_declare(queue='hello')

channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='One more body!!!')
print(" [x] Sent 'Hello World!'")

connection.close()
