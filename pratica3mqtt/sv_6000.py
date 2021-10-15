import paho.mqtt.client as mqtt 
from struct import pack 
from random import randint 
from time import sleep 

AREA_ID = 10 
SENSOR_ID = 6000  #arquivo sv_6000.py e outro sv_5000

# topicos providos por este sensor 
tt = "area/%d/sensor/%s/temperatura" % (AREA_ID,SENSOR_ID) 

# cria um identificador baseado no id do sensor 
client = mqtt.Client(client_id = 'NODE:%d-%d' % (AREA_ID,SENSOR_ID), 
                    protocol = mqtt.MQTTv31) 
# conecta no broker
client.connect("127.0.0.1", 1883)

while True:
   # gera um valor de temperartura aleatorio
   t = randint(0,50)
   msg = str(t)
   # envia a publicacao
   client.publish(tt,msg,qos=0)
   print (tt + "/" + str(t))
   sleep(5)
