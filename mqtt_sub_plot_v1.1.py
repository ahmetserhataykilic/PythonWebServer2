#!usr/bin/env python

import pika
from pika import channel
#---------------------------------------
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import csv

from pika.connection import Parameters
#---------------------------------------

column = []
j=0

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost')
)

channel = connection.channel()

#def x(i):



# def my_callback_with_extended_args(ch, method, properties, body, j):
#     print(j)



def callback(ch,method,properties,body):
    print("[x] Received %r" % body)
    print(body)
    a = str(body[0:2])
    a = a[2:4]
    print(a)
    b = str(body[3:7])
    b = b[2:6]
    print(b)

    print(j)

    # if k >= 4:
    #     print("asdfasdfasdfasd")
    #     fname = "output_3.csv"
    #     file = open(fname,"w",encoding="utf-8")
    #     # create the csv writer
    #     writer = csv.writer(file)
    #     # write a row to the csv file
    #     writer.writerow([str(a),str(b)])
    #     #file.close()

# channel.basic_consume(
#   lambda ch, method, properties, body: my_callback_with_extended_args(ch, method, properties, body, j=3),
#   queue='esp8266.test',
#   no_ack=True)

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
