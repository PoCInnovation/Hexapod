const byte TRIGGER_PIN = 2; // Broche TRIGGER
const byte ECHO_PIN = 3;    // Broche ECHO

void init_ultrassound()
{
	pinMode(TRIGGER_PIN, OUTPUT);
  	digitalWrite(TRIGGER_PIN, LOW); // La broche TRIGGER doit être à LOW au repos
  	pinMode(ECHO_PIN, INPUT);
}

float get_ultrassound_data()
{
	const unsigned long MEASURE_TIMEOUT = 25000UL; // 25ms = ~8m à 340m/s
	const float SOUND_SPEED = 340.0 / 1000;

 	/* 1. Lance une mesure de distance en envoyant une impulsion HIGH de 10µs sur la broche TRIGGER */
	digitalWrite(TRIGGER_PIN, HIGH);
	delayMicroseconds(10);
	digitalWrite(TRIGGER_PIN, LOW);
  	long measure = pulseIn(ECHO_PIN, HIGH, MEASURE_TIMEOUT);
	float distance_mm = measure / 2.0 * SOUND_SPEED;
	return distance_mm;
}

void setup()
{
	Serial.begin(115200);
	init_ultrassound();
}

void loop()
{
	float distance_mm = get_ultrassound_data();
	Serial.print(distance_mm / 10.0, 2);
 	Serial.print(F("cm, \n"));

  	delay(500);
}
