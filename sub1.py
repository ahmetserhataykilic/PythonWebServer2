# mqtt_sub.py - Python MQTT subscribe example 
#
import paho.mqtt.client as mqtt
 
def on_connect(client, userdata, flags, rc):
    print("Connected to broker")
 
def on_message(client, userdata, message):
    print ("Message received: "  + message.payload)

client = mqtt.Client()
client.username_pw_set("ahmet", password='1q2w3e4r')
client.connect("192.168.1.8", 5672) 

client.on_connect = on_connect       #attach function to callback
client.on_message = on_message       #attach function to callback

client.subscribe("esp8266.test") 
client.loop_forever()                 #start the loop