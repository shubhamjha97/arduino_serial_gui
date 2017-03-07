int led=13;
char serialChar=0;

void setup()
{
  pinMode(led, OUTPUT);
  Serial.begin(9600);
  Serial.println("Beginning serial");
}

void loop()
{
  serialChar=0;
  int stat;
  if(Serial.available()>0){
        stat=(int)Serial.read();
        stat=stat-48;
        Serial.println(stat, DEC);
        if(stat==0){
          digitalWrite(led, LOW);
          delay(100);
          }
        else{
          digitalWrite(led, HIGH);
          delay(100);
        }
  }
}
