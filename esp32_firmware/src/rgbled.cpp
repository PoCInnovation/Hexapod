#include "rgbled.hpp"

RGBled::RGBled(uint8_t pinR, uint8_t pinG, uint8_t pinB)
{
    _pinR = pinR;
    _pinG = pinG;
    _pinB = pinB;

    pinMode(_pinR, OUTPUT);
    pinMode(_pinG, OUTPUT);
    pinMode(_pinB, OUTPUT);
}

void RGBled::setColor(uint8_t r, uint8_t g, uint8_t b)
{

}

void RGBled::test()
{
    while (1) {
        digitalWrite(_pinR, HIGH);
        delay(1000);
        digitalWrite(_pinR, LOW);
        digitalWrite(_pinG, HIGH);
        delay(1000);
        digitalWrite(_pinG, LOW);
        digitalWrite(_pinB, HIGH);
        delay(1000);
        digitalWrite(_pinB, LOW);
    }
}