#ifndef ULTRASOUND_HPP
#define ULTRASOUND_HPP

#include <Arduino.h>

class Ultrasound {
public:
    Ultrasound(byte triggerPin, byte echoPin);
    ~Ultrasound() = default;
    float getDistance();

private:
    byte _triggerPin;
    byte _echoPin;
};

#endif /* ULTRASOUND_HPP */
