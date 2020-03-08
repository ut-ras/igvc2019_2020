
void setup() {
  pinMode(17, OUTPUT);
  pinMode(18, OUTPUT);
  pinMode(19, OUTPUT);
  pinMode(20, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  while(Serial.available() == 0);
  int a0 = Serial.parseInt();
  int a1 = Serial.parseInt();
  int a2 = Serial.parseInt();
  int a3 = Serial.parseInt();
  int a4 = Serial.parseInt();
  int a5 = Serial.parseInt();
  if (a2 == 1) digitalWrite(17, HIGH);
  else digitalWrite(17, LOW);
  if (a3 == 1) digitalWrite(18, HIGH);
  else digitalWrite(18, LOW);
  if (a4 == 1) digitalWrite(19, HIGH);
  else digitalWrite(19, LOW);
  if (a5 == 1) digitalWrite(20, HIGH);
  else digitalWrite(20, LOW);
  Serial.print(a0);
  Serial.print(a1);
  Serial.print(a2);
  Serial.print(a3);
  Serial.print(a4);
  Serial.println(a5);
}
