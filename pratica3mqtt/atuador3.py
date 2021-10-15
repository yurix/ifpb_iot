import paho.mqtt.client as mqtt 
from time import time, sleep 
import socket 
import uuid 

def on_connect(client, userdata, flags, rc): 
  client.subscribe('/L1') 

def on_message(client, userdata, message): 
  msg = message.payload.decode('utf-8') 
  #recebeu mensagem entao encaminha para Server.py 
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
  s.connect(('127.0.0.1', 50000)) 
  msg = 'L1' 
  s.sendall(msg.encode('ascii')) 
  data = s.recv(1024) 
  s.close() 
  print('Received to send:')
  print(msg) 

client = mqtt.Client() 
client.on_connect = on_connect 
client.on_message = on_message 
client.connect("127.0.0.1",1883) 
client.loop_forever() 

