#!usr/bin/env python

import pika
from pika import channel

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost')
)



channel = connection.channel()
channel.queue_declare(queue = 'esp8266.pub',durable='True', auto_delete='False')
channel.basic_publish(exchange='amq.topic', routing_key='esp8266.test', body="hello world!")
#channel.close()

def callback(ch,method,properties,body):
    print("[x] Received %r" % body)
    
# channel = connection.channel()

# def callback(ch,method,properties,body):
#     print("[x] Received %r" % body)

# channel.basic_consume(
#     queue='mqtt-subscription-ESP8266Clientqos0', on_message_callback=callback, auto_ack=True
# )

# print('[X] Waiting for messages to exit press ctrl +c')
# channel.start_consuming()