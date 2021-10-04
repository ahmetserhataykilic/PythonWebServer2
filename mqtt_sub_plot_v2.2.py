
#!usr/bin/env python

import pika
from pika import channel
#---------------------------------------
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import csv
import time
import threading
import plotly.express as px
from plotly.offline import plot
import plotly.io as pio
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import urllib
#import urllib2
#---------------------------------------

a=0
column = np.array([['x','y'],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]])

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost')
)

channel = connection.channel()
driver = webdriver.Chrome("C:/Users/ASAykilic/Desktop/webServer/PythonWebServer/chromedriver.exe")
driver.get('file:///C:/Users/ASAykilic/Desktop/webServer/PythonWebServer/temp-plot.html')

roww = 0
def asa(qwe):
    #df = px.data.tips()
    #fd = px.data.iris()
    #fig = px.scatter_matrix(fd, dimensions=["sepal_width", "sepal_length", "petal_width", "petal_length"], color="species")
    #fig = px.line(df, x = 'x', y = 'y', title='Apple Share Prices over time (2014)')

    fname = "points.csv"
    with open(fname,"w",encoding="utf-8") as file:
        csv_file = csv.writer(file)
        csv_file.writerow(['x','y'])
        csv_file.writerow(['17','4000'])
        csv_file.writerow(['17','0'])
        for roww in range(1,17):
            #print(qwe)
            a=int(qwe[[roww],[0]])
            b=int(qwe[[roww],[1]])
            csv_file.writerow([str(a),str(b)])

    df = pd.read_csv("points.csv")
    fig = px.scatter(df, x="x", y="y", title='PROXIMITY')
    pio.renderers.default = 'browser'
    # with open('temp-plot.html','w') as f_html:
    #     f_html.write(html)
    plot(fig)
    driver.get('file:///C:/Users/ASAykilic/Desktop/webServer/PythonWebServer/temp-plot.html')
    #driver.refresh()





    #fig.show()
    #---------------------------------------
    #---------------------------------------
    # dataset = pd.read_csv('output_3.csv')
    # X = dataset.iloc[:, 0:1].values
    # Y = dataset.iloc[:, 1:2].values

    # # Design a chart
    # plt.scatter(X, Y, label = 'Point (X;Y)', color = 'k')
    # plt.xlabel('X')
    # plt.ylabel('Y')
    # plt.title('points')
    # plt.legend()
    # plt.draw()
    # plt.show()
    # #plt.close(plt)



max = False
min = True

def callback(ch,method,properties,body):
    #print("[x] Received %r" % body)
    intBody = int(body)
    lenBody = len(str(intBody))
    print("intBody : %r" % intBody)
    #print(len(str(intBody)))
    global max, min, a
    x = 'x'
    y = 'y'
    if lenBody <= 2 and intBody != 0 and intBody < 17:
        a = intBody
        print("a : %r" % a)
        column[[intBody],[0]]=intBody

    if lenBody > 2:
        column[[a],[1]]=intBody
        if a == 16 and max == False:

            column[[0],[0]] = str(x)
            column[[0],[1]] = str(y)
            qwe=column
            print(column)
            asa(qwe)
            # max = True
            # min = False
        # if a == 1 and min == False:
        #     column[[0],[0]] = str(x)
        #     column[[0],[1]] = str(y)
        #     qwe=column
        #     print(column)
        #     asa(qwe)
        #     max = False
        #     min = True
    # print(body)
    # a = str(body[0:2])
    # a = a[2:4]
    # intA = int(a)
    # print(intA)
    # b = str(body[3:7])
    # b = b[2:6]
    # intB = int(b)
    # print(intB)
    # column[[intA],[0]]=intA
    # column[[intA],[1]]=intB

    #time.sleep(5)


channel.basic_consume(
    queue='esp8266.test', on_message_callback=callback, auto_ack=True
)

print('[*] Waiting for messages to exit press ctrl +c')
channel.start_consuming()

