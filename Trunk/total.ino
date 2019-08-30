int buzzPin =  13;
int i;

int inputPin = 2;
int val = 0;
int state = 0;

void setup() {
  pinMode(inputPin, INPUT);
  
  Serial.begin(9600);

  pinMode(5,OUTPUT);  
  pinMode(6,OUTPUT);  
  pinMode(7,OUTPUT);  
  pinMode(8,OUTPUT);  
  digitalWrite(7,HIGH);  
  digitalWrite(8,HIGH);  
}

void loop() {
  val = digitalRead(inputPin);
  if (val == HIGH){
    Serial.println("Motion detected!");
    if (state == 0){
      Serial.println("OUT!");
      digitalWrite(6,LOW);  
      analogWrite(5,255);  
      for (i=0 ; i<3 ; i++){
        tone(buzzPin,1046,1000); // 레
        delay(1000);
        noTone(buzzPin);
        delay(1000);  
      }
      analogWrite(5,0);  
      delay(2000);
      state = 1;
    } else if (state == 1) {
      Serial.println("IN!");
      digitalWrite(5,LOW);  
      analogWrite(6,255);  
      for (i=0 ; i<3 ; i++){
        tone(buzzPin,1046,1000); // 레
        delay(1000);
        noTone(buzzPin);
        delay(1000);  
      }  
      analogWrite(6,0);  
      delay(2000);
      state = 0;
    }
    
    
  } else {
    Serial.println("Motion ended!");
    
    
  }
  Serial.println(" ");
  Serial.println("---------");

}
