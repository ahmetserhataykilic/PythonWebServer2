#!usr/bin/env python

import pika
from pika import channel
#---------------------------------------
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import csv
import time
#---------------------------------------
i=0
j=0

column = np.array([[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]])

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost')
)

channel = connection.channel()


# def x(j):
#     j=j+1
roww = 0
maxRow = 11
def asa(qwe):
    fname = "output_3.csv"
    with open(fname,"w",encoding="utf-8") as file:
        csv_file = csv.writer(file)
        for roww in range(0,12):
            print(qwe)
            a=int(qwe[[roww],[0]])
            b=int(qwe[[roww],[1]])
            csv_file.writerow([str(a),str(b)])

    #---------------------------------------
    #---------------------------------------
    dataset = pd.read_csv('output_3.csv')
    X = dataset.iloc[:, 0:1].values
    Y = dataset.iloc[:, 1:2].values

    # Design a chart
    plt.scatter(X, Y, label = 'Point (X;Y)', color = 'k')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('points')
    plt.legend()
    plt.show()



def callback(ch,method,properties,body):
    print("[x] Received %r" % body)
    print(body)
    a = str(body[0:2])
    a = a[2:4]
    intA = int(a)
    print(intA)
    b = str(body[3:7])
    b = b[2:6]
    intB = int(b)
    print(intB)
    column[[intA],[0]]=intA
    column[[intA],[1]]=intB
    print(column)
    
    qwe=column
    print(column)
    if a == '11':
        # time.sleep(5)
        asa(qwe)


channel.basic_consume(
    queue='esp8266.test', on_message_callback=callback, auto_ack=True
)

print('[*] Waiting for messages to exit press ctrl +c')
channel.start_consuming()

