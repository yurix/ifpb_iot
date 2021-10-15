import paho.mqtt.client as mqtt
from time import time, sleep
import uuid

def on_connect(client, userdata, flags, rc):
   client.subscribe(topic)

def on_message(client, userdata, message):
   msg = message.payload.decode('utf-8')
   print(msg)

topic = "/atuador"
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect("127.0.0.1",1883)
client.loop_forever()
