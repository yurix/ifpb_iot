from coapdtlsclient import coapDtlsClient
from uuid import getnode as get_mac
import time
import os

#Temperature sensor file
#SENSOR MAC_SENSOR TEMP FLUXO GPS TEMPO
def mountPayload(sensorId, sensorMac, temp, flow, gps, timestamp):
  payload = sensorId
  payload += '/'+sensorMac
  payload += '/'+temp
  payload += '/'+flow
  payload += '/'+gps
  payload += '/'+timestamp
  print(payload)
  return payload

ciphers = "ECDHE+AESGCM"
clienteDtls = coapDtlsClient("127.0.0.1", 5684, ciphers).client
#temperatureSensor = TempSensor(temp_file);
try:
 #while True:
  temperature = "32"#str(temperatureSensor.read_temp());
  macAddress = str(get_mac())
  timestamp = str(time.time())
  payload = mountPayload("SENSOR_JOHANN", macAddress, temperature,str(0), "NaMinhaCasa", timestamp)
  tInicio = time.time()
  response = clienteDtls.post("gpsflowtemp", payload)
  tFim = time.time()
  print("Post demorou %f ms na configuracao %s" % (tFim - tInicio,ciphers))
  print(response.pretty_print())
  #time.sleep(60)
  #forcar parada
  clienteDtls.stop()
  os.system('kill %d' % os.getpid())

except KeyboardInterrupt:
 print("cliente stopped")
 clienteDtls.stop()
 print("Exiting...")
