#include "Ultrasound.hpp"

Ultrasound::Ultrasound(byte triggerPin, byte echoPin) : _triggerPin(triggerPin), _echoPin(echoPin)
{
    pinMode(_triggerPin, OUTPUT);
    digitalWrite(_triggerPin, LOW);
    pinMode(_echoPin, INPUT);
    Serial.println("Ultrassounds pins init done");
}

float Ultrasound::getDistance()
{
    const unsigned long MEASURE_TIMEOUT = 25000UL;
    const float SOUND_SPEED = 340.0 / 1000;

    digitalWrite(_triggerPin, HIGH);
    delayMicroseconds(10);
    digitalWrite(_triggerPin, LOW);
    long measure = pulseIn(_echoPin, HIGH, MEASURE_TIMEOUT);
    return measure / 2.0 * SOUND_SPEED;
}
