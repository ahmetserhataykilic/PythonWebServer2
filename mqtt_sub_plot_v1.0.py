#!usr/bin/env python

import pika
from pika import channel
#---------------------------------------
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import csv

#---------------------------------------


connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost')
)

channel = connection.channel()

def callback(ch,method,properties,body):
    print("[x] Received %r" % body)
    a = chr(body[0])
    b = chr(body[2])
    print(a)
    print(b)
    
    f = open('points.csv', 'w') 
    # create the csv writer
    writer = csv.writer(f)
    # write a row to the csv file
    writer.writerow([a,b])
    f.close()

channel.basic_consume(
    queue='esp8266.test', on_message_callback=callback, auto_ack=True
)

print('[*] Waiting for messages to exit press ctrl +c')
channel.start_consuming()


#---------------------------------------
#---------------------------------------


# dataset = pd.read_csv('points.csv')
# X = dataset.iloc[:, 0:1].values
# Y = dataset.iloc[:, 1:2].values

# # Design a chart
# plt.scatter(X, Y, label = 'Point (X;Y)', color = 'k')
# plt.xlabel('X')
# plt.ylabel('Y')
# plt.title('points')
# plt.legend()
# plt.show()
