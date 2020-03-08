
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
  value_zero = analogRead(analogInput_zero);
  value_one = analogRead(analogInput_one);
    //Serial.println(value_zero);
  Serial.println(value_zero);
  Serial.println(value_one);
  Serial.println(digitalRead(up));
  Serial.println(digitalRead(down));
  Serial.println(digitalRead(left));
  Serial.println(digitalRead(right));
  delay(200);

  
  
}
