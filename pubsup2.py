import paho.mqtt.client as mqttclient
import time

def on_connect(client,userdata,flags,rc):
    if rc==0:
        print("client is connected")
        global connected 
        connected = True
    else:
        print("connection failed")

connected = False
broker_address = "192.168.1.8"
port = 5672
user = "ahmet"
password = "1q2w3e4r"

client = mqttclient.Client("MQTT")
client.username_pw_set(user,password=password)
client.on_connect = on_connect
client.connect(broker_address, port=port)
client.loop_start()

while connected!=True:
    time.sleep(0.2)
    print("qqwd")

client.publish("mqtt/firstcode","hello MQTT, python")
client.loop_stop()
print("asdfasdf")