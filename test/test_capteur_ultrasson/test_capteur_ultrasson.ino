int trigPin = 6;
int echoPin = 7;
long duration, cm;
int ledPin = 8;

void setup(void) {
  Serial.begin (9600);
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
  pinMode(ledPin, OUTPUT);
}

long get_ultrasonic_sensor_distance(int trig_pin, int echo_pin)
{
  digitalWrite(trigPin, LOW);
  delayMicroseconds(5);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
  pinMode(echoPin, INPUT);
  duration = pulseIn(echoPin, HIGH);
  // Convert the time into a distance
  cm = (duration/2) / 29.1;
  return (cm);
}

void loop(void) {
  cm = get_ultrasonic_sensor_distance(trigPin, echoPin);
  if (cm < 50)
  	digitalWrite(ledPin, HIGH);
  else
    	digitalWrite(ledPin, LOW);
  delay(250);
}