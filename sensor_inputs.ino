#include "Arduino.h"
#include "DHT.h"


dht DHT;

#define RE 6
#define DE 7

#define DHT11_PIN 8

//npk sensor
//const byte nitro[] = {0x01, 0x03, 0x00, 0x1e, 0x00, 0x01, 0xe4, 0x0c};
//const byte phos[] = {0x01, 0x03, 0x00, 0x1f, 0x00, 0x01, 0xb5, 0xcc};
//const byte pota[] = {0x01, 0x03, 0x00, 0x20, 0x00, 0x01, 0x85, 0xc0};
 
byte values[11];

void setup ( ) {
      Serial.begin (9600); 
      mod.begin(9600);
      pinMode (trigger_pin, OUTPUT); 
      pinMode (echo_pin, INPUT);
      pinMode(RE, OUTPUT);
      pinMode(DE, OUTPUT);
      
      Serial.println("temperature");
      Serial.println(", ");
      Serial.println("humidity");
      Serial.println(", ");
      Serial.println("ph");
      
}
void loop ( ) {

   
    //DHT11
    int chk = DHT.read11(DHT11_PIN);
    delay(1000);

     //pH METER
     for(int i=0;i<10;i++) 
     { 
       buffer_arr[i]=analogRead(A0);
       delay(30);
     }
     for(int i=0;i<9;i++){
        for(int j=i+1;j<10;j++){
          if(buffer_arr[i]>buffer_arr[j]){
            temp=buffer_arr[i];
            buffer_arr[i]=buffer_arr[j];
            buffer_arr[j]=temp;
          }
        }
      }
      avgval=0;
      for(int i=2;i<8;i++)
        avgval+=buffer_arr[i];
      float volt=(float)avgval*5.0/1024/6;
      float ph_act = -5.70 * volt + calibration_value;
      //Serial.print(ph_act);
      delay(1000);
      Serial.print(DHT.temperature);
      Serial.print(", ");
      Serial.print(DHT.humidity);
      Serial.print(", ");
      Serial.print(ph_act);
      Serial.println();
}
