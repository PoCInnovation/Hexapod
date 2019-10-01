#ifndef ULTRASOUND_H
#define ULTRASOUND_H

#include <SoftwareSerial.h>

class Ultrasound
{
private:
    byte m_triggerPin; // 13
    byte m_echoPin;    // 12

public:
    Ultrasound(byte triggerPin, byte echoPin);
    ~Ultrasound();
    void init();
    float get_data();
};

#endif