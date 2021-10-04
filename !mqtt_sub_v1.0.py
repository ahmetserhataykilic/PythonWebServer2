#!usr/bin/env python

import pika
from pika import channel
import datetime

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost')
)

channel = connection.channel()
gelenDataSayisi = 0

def callback(ch,method,properties,body):
    now = datetime.datetime.now()
    print(now.strftime("%H:%M:%S"))
    print("[x] Received %r" % body)
    
    file1 = open("MyFile2.txt","a")
    file1.write(now.strftime("%H:%M:%S"))
    file1.write(" - ")
    file1.write(str(body))
    file1.write("\n")

    global gelenDataSayisi
    gelenDataSayisi += 1
    if(gelenDataSayisi ==4):
        gelenDataSayisi = 0
        file1 = open("MyFile2.txt","a")
        file1.write("\n")
    #print(int(body))
    
channel.basic_consume(
    queue='esp8266.sub', on_message_callback=callback, auto_ack=True
)

print('[*] Waiting for messages to exit press ctrl +c')
channel.start_consuming()




