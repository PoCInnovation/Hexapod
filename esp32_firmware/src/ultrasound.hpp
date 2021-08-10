#ifndef ULTRASOUND_HPP
#define ULTRASOUND_HPP

#include "Arduino.h"

class Ultrasound {
  private:
    byte _trigger_pin;
    byte _echo_pin;

  public:
    Ultrasound(byte trigger_pin, byte echo_pin);
    float getDistance();
};

#endif /* ULTRASOUND_HPP */
