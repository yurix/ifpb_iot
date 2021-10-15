import socket
import serial
HOST = '127.0.01'
PORT = 50000
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
orig = (HOST, PORT)
tcp.bind(orig)
tcp.listen(1)
usb = serial.Serial ( '/dev/ttyUSB0')


while True:
    con, cliente = tcp.accept()
    print ('Conectado')
    while True:
        msg = con.recv(1024)
        if not msg: break
        message = str(msg.decode())
        print(message)
        usb.write(bytes(message, 'utf-8'))
    print('Finalizando conexao do cliente')
    con.close()
    usb.close()