#include "ultrasound.hpp"

Ultrasound::Ultrasound(byte trigger_pin, byte echo_pin) : _trigger_pin(trigger_pin), _echo_pin(echo_pin)
{
    pinMode(_trigger_pin, OUTPUT);
    digitalWrite(_trigger_pin, LOW);
    pinMode(_echo_pin, INPUT);
}

float Ultrasound::getDistance()
{
    const unsigned long MEASURE_TIMEOUT = 25000UL;
    const float SOUND_SPEED = 340.0 / 1000;

    digitalWrite(_trigger_pin, HIGH);
    delayMicroseconds(10);
    digitalWrite(_trigger_pin, LOW);
    long measure = pulseIn(_echo_pin, HIGH, MEASURE_TIMEOUT);
    return measure / 2.0 * SOUND_SPEED;
}