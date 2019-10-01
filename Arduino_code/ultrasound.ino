#include "ultrasound.h"

ultrassound::Ultrasound(byte triggerPin, byte echoPin)
{
    m_triggerPin = triggerPin;
    m_echoPin = echoPin;
}

Ultrasound::~Ultrasound() {}

void Ultrasound::init()
{
    pinMode(m_triggerPin, OUTPUT);
    digitalWrite(m_triggerPin, LOW);
    pinMode(m_echoPin, INPUT);
    Serial.println("Ultrassounds pins init done");
}

// see : https://randomnerdtutorials.com/complete-guide-for-ultrasonic-sensor-hc-sr04/
float Ultrasound::get_data()
{
    const unsigned long MEASURE_TIMEOUT = 25000UL;
    const float SOUND_SPEED = 340.0 / 1000;
    long mesure;

    digitalWrite(m_triggerPin, HIGH);
    delayMicroseconds(10);
    digitalWrite(m_triggerPin, LOW);

    measure = pulseIn(m_echoPin, HIGH, MEASURE_TIMEOUT);
    return measure / 2.0 * SOUND_SPEED;
}
