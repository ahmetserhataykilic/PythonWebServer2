#!usr/bin/env python

import pika
from pika import channel
import datetime

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost')
)

channel = connection.channel()


def callback(ch,method,properties,body):
    now = datetime.datetime.now()
    print(now.strftime("%H:%M:%S"))
    print("[x] Received %r" % body)
    
    file1 = open("MyFile2.txt","a")
    file1.write(now.strftime("%H:%M:%S"))
    file1.write(" - ")
    file1.write(str(body))
    file1.write("\n")
    #print(len(str(body)))
    if(len(str(body)) > 8):
        file1.write("\n")

    
    #print(int(body))
    
channel.basic_consume(
    queue='esp8266.sub2_light', on_message_callback=callback, auto_ack=True
)

print('[*] Waiting for messages to exit press ctrl +c')
channel.start_consuming()




