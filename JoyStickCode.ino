
int analogInput_zero = 0;
int analogInput_one = 1;
int value_zero = 0;
int value_one = 0;
String numbers = String();
int up = 3;
int right = 4;
int down = 5;
int left = 6;

void setup() {
  Serial.begin(9600);
  pinMode(analogInput_zero, INPUT); //Vertical
  pinMode(analogInput_one, INPUT); //Horizontal
  pinMode(up, INPUT);
  pinMode(right, INPUT);
  pinMode(left, INPUT);
  pinMode(down, INPUT);
  
}
void loop()
{
  value_zero = analogRead(analogInput_zero)/103;
  value_one = analogRead(analogInput_one)/103;
    //Serial.println(value_zero);
  Serial.print(value_zero);
  Serial.print(",");
  Serial.print(value_one);
  Serial.print(",");
  Serial.print(digitalRead(up));
  Serial.print(",");
  Serial.print(digitalRead(down));
  Serial.print(",");
  Serial.print(digitalRead(left));
  Serial.print(",");
  Serial.println(digitalRead(right));

  
  
}
