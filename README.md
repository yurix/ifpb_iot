# ifpb_iot

Objetivo

O objetivo desta atividade é utilizar a porta serial (USB) como caminho de comunicação entre o computador e o Arduino. 


== Exercício 1 ==

Implantar o código que realiza um loop escrevendo uma mensagem na porta serial do Arduino para o Computador.  

1. Habilitar a porta serial para comunicação (Caso seja a primeira vez)

> Selecionar a porta ttyUSB0 para comunicação com o Arduino Uno.

Mensagem no Console:

Erro abrindo a porta serial "/dev/ttyUSB0". Tente consultar a documentação em http://playground.arduino.cc/Linux/All#Permission

> Terminal:

$ ls -l /dev/ttyUSB*

crw-rw---- 1 root dialout 188, 0 set 20 11:05 /dev/ttyUSB0

$ sudo usermod -a -G dialout yuri

$ shutdown -r now 

2. Abrir o Monitor Serial (Ferramentas -> Monitor Serial)
3. Copiar o código (exercicio1.c) e implantar no Arduino.



== Exercício 2 ==


Implantar o código que realiza um loop lendo uma mensagem na porta serial do Computador para o Arduino.  


1. Abrir o Monitor Serial (Ferramentas -> Monitor Serial)
2. Copiar o código (exercicio2.c) e implantar no Arduino.


== Exercicio 3 ==

Ler a porta serial a partir de uma aplicação feita em python

1. Implantar o código do exercicio1.c no arduino
2. Instalar a biblioteca PySerial

$ pip install pyserial

3. Executar o código em python exercicio3.py

$ python3 exercicio3.py

