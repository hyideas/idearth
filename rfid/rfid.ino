#include <SPI.h>
#include <MFRC522.h>

const int trigPin1 = 30;
const int echoPin1 = 31;

const int trigPin2 = 32;
const int echoPin2 = 33;

#define SS_PIN 20
#define RST_PIN 9
#define BUZ 3
#define LED 2

int value = 0;
int balue;
long duration1, distance1, duration2, distance2;

// 라이브러리 생성
MFRC522 rfid(SS_PIN, RST_PIN); // Instance of the class

MFRC522::MIFARE_Key key; 

//이전 ID와 비교하기위한 변수
byte nuidPICC[4];


void setup() {

  Serial.begin(9600);
  pinMode(BUZ, OUTPUT);
  pinMode(trigPin1, OUTPUT);
  pinMode(echoPin1, INPUT);
  pinMode(trigPin2, OUTPUT);
  pinMode(echoPin2, INPUT);
  pinMode(LED, OUTPUT);
  
  for (byte i = 0; i < 6; i++) {
    key.keyByte[i] = 0xFF;
  }
  
  Serial.println(F("This code scan the MIFARE Classsic NUID."));
  Serial.print(F("Using the following key:"));
  printHex(key.keyByte, MFRC522::MF_KEY_SIZE);


}

void loop() {
  //Serial.println(digitalRead(BUTTON));
  //delay(100);
    SPI.begin(); // SPI 시작
    rfid.PCD_Init(); // RFID 시작
    if ( ! rfid.PICC_IsNewCardPresent()){
      balue = 0 ;
      Serial.println("OFF");
      return;
    }
  
    // ID가 읽혀졌다면 다음으로 넘어가고 아니면 더이상 
    // 실행 안하고 리턴
    if ( ! rfid.PICC_ReadCardSerial())
      return;
  
    Serial.print(F("PICC type: "));
  
    //카드의 타입을 읽어온다.
    MFRC522::PICC_Type piccType = rfid.PICC_GetType(rfid.uid.sak);
  
    //모니터에 출력
    Serial.println(rfid.PICC_GetTypeName(piccType));
  
    // MIFARE 방식인지 확인하고 아니면 리턴
    if (piccType != MFRC522::PICC_TYPE_MIFARE_MINI &&  
      piccType != MFRC522::PICC_TYPE_MIFARE_1K &&
      piccType != MFRC522::PICC_TYPE_MIFARE_4K) {
      Serial.println(F("Your tag is not of type MIFARE Classic."));
      return;
    }
  
    // 만약 바로 전에 인식한 RF 카드와 다르다면..
    if (rfid.uid.uidByte[0] != nuidPICC[0] || 
      rfid.uid.uidByte[1] != nuidPICC[1] || 
      rfid.uid.uidByte[2] != nuidPICC[2] || 
      rfid.uid.uidByte[3] != nuidPICC[3] ) {
      Serial.println(F("A new card has been detected."));
  
      // ID를 저장해둔다.    
      for (byte i = 0; i < 4; i++) {
        nuidPICC[i] = rfid.uid.uidByte[i];
      }
     
      //모니터 출력
      Serial.println(F("The NUID tag is:"));
  
      Serial.print(F("In hex: "));
      //16진수로 변환해서 출력
      printHex(rfid.uid.uidByte, rfid.uid.size);
      Serial.println();
  
  
      Serial.print(F("In dec: "));
      //10진수로 출력
      printDec(rfid.uid.uidByte, rfid.uid.size);
      Serial.println();
    }
    else {
      balue = 1 ;
      Serial.println("ON");
      Serial.println(F("Card read previously.")); //바로 전에 인식한 것과 동일하다면 
    }
  
    // PICC 종료
    rfid.PICC_HaltA();
  
    // 암호화 종료(?)
    rfid.PCD_StopCrypto1();

    
    if (balue == 1){
        
      digitalWrite(trigPin1, LOW);
      delayMicroseconds(2);
      digitalWrite(trigPin1, HIGH);
      delayMicroseconds(5);
      digitalWrite(trigPin1, LOW);
      duration1 = pulseIn(echoPin1, HIGH);
    
      digitalWrite(trigPin2, LOW);
      delayMicroseconds(2);
      digitalWrite(trigPin2, HIGH);
      delayMicroseconds(5);
      digitalWrite(trigPin2, LOW);
      duration2 = pulseIn(echoPin2, HIGH);
     
      long distance1 = duration1 /58.2;
      long distance2 = duration2 /58.2;
    
      Serial.print("A ");
      Serial.println(distance1);
      Serial.print("B ");
      Serial.println(distance2);
    
      if ((distance1 < 15 ) || (distance2 < 15 )){ 
          digitalWrite(LED, HIGH);
          tone(BUZ, 3000, 50);
          delay(50);
          digitalWrite(LED, LOW);
          noTone(BUZ);
          delay(50);
      }
    
      else if (((distance1 < 30 ) && (distance1 > 15)) || ((distance2 < 30 ) && (distance2 > 15))){ 
          digitalWrite(LED, HIGH);
          tone(BUZ, 3000, 100);
          delay(100);
          digitalWrite(LED, LOW);
          noTone(BUZ);
          delay(100);
      }
    
      else if (((distance1 < 45 ) && (distance1 > 30)) || ((distance2 < 45 ) && (distance2 > 30))){ 
          digitalWrite(LED, HIGH);
          tone(BUZ, 3000, 150);
          delay(150);
          digitalWrite(LED, LOW);
          noTone(BUZ);
          delay(150);
      }
    }
  }

  void printHex(byte *buffer, byte bufferSize) {
  for (byte i = 0; i < bufferSize; i++) {
    Serial.print(buffer[i] < 0x10 ? " 0" : " ");
    Serial.print(buffer[i], HEX);
  }
}

//10진수로 변환하는 함수
void printDec(byte *buffer, byte bufferSize) {
  for (byte i = 0; i < bufferSize; i++) {
    Serial.print(buffer[i] < 0x10 ? " 0" : " ");
    Serial.print(buffer[i], DEC);
  }
}
  
