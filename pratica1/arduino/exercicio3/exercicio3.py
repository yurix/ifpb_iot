import serial

i = int(0)

while i < 20:
    ser = serial.Serial ( '/dev/ttyUSB0')
    linhaLida = ser.readline()
    print (linhaLida)
    i = i + 1
    ser.close()


    