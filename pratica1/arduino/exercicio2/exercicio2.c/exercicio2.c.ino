achar ch;

void setup() {
  Serial.begin(9600);
}

void loop() {
  while(Serial.available() == 0) {
    Serial.println("Informe um caractere: ");
    delay(300);
  }

  ch = Serial.read();
  Serial.print("ch = ");
  Serial.println(ch);
  delay(2000);
}
