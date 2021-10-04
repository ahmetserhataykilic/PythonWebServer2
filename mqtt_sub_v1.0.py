#!usr/bin/env python

import pika
from pika import channel


connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost')
)

channel = connection.channel()

def callback(ch,method,properties,body):
    print("[x] Received %r" % body)

channel.basic_consume(
    queue='esp8266.test', on_message_callback=callback, auto_ack=True
)

print('[*] Waiting for messages to exit press ctrl +c')
channel.start_consuming()




