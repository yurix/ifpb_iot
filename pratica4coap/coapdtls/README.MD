Como criar a imagem docker coapserver:

1) $ sudo docker build -t coapserver .
2) $ sudo docker run -it --rm coapserver /bin/bash

Interno ao container coapserver

1) $ python coapdtlsserver.py & 
2) $ python maincoap.py
