#!usr/bin/env python

import pika
from pika import channel
import datetime

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost')
)

channel = connection.channel()

def callback(ch,method,properties,body):
    print("[x] Received %r" % body)
    
    #print(int(body))
    
channel.basic_consume(
    queue='esp8266.sub2_light', on_message_callback=callback, auto_ack=True
)

print('[*] Waiting for messages to exit press ctrl +c')
channel.start_consuming()




