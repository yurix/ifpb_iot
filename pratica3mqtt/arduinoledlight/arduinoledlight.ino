const int led = 8; //constante led refere-se ao pino digital 8.
int estadoler = 10;
// the setup routine runs once when you press reset:
void setup() {
 // initialize serial communication at 9600 bits per second:
 Serial.begin(9600);
 pinMode(led,OUTPUT); //Definindo pino digital 8 como de saída.
 while (!Serial) {
 ; // wait for serial port to connect. Needed for native USB port only
 }
}

/** * Função que lê uma string da Serial * e retorna-a */
String leStringSerial(){
String conteudo = "";
char caractere;
 while(Serial.available() > 0) { // Enquanto receber algo pela serial
  caractere = Serial.read(); // Lê byte da serial
  if (caractere != '\n'){ // Ignora caractere de quebra de linha
  conteudo.concat(caractere); // Concatena valores
  }
  delay(10); // Aguarda buffer serial ler próximo caractere
 }
Serial.print("Recebi: ");
Serial.println(conteudo);
return conteudo;
}
void loop() {
 while (Serial.available() > 0) { // read the input on analog pin 0:
 int est = digitalRead(led);
 String recebido = leStringSerial(); // Lê toda string recebida
 if(recebido=="L1"){ //ou seja, enviar o número 1
 if (est == 0) {
  Serial.println("Led aceso");
 digitalWrite(led,HIGH); //Botão pressionado, acende o led.
 } else if (est == 1) {
  Serial.println("Led apagado");

 digitalWrite(led,LOW); //Botão pressionado, acende o led.
 }
 }
 delay(1); // delay in between reads for stability
 }
 }
