#ifndef RGBLED_HPP
#define RGBLED_HPP

#include <Arduino.h>

#define RGB_RED 255, 0, 0
#define RGB_GREEN 0, 255, 0
#define RGB_BLUE 0, 0, 255

class RGBled {
  private:
    uint8_t _pinR;
    uint8_t _pinG;
    uint8_t _pinB;

  public:
    RGBled(uint8_t pinR, uint8_t pinG, uint8_t pinB);
    void setColor(uint8_t r, uint8_t g, uint8_t b);
    void test();
    void turnOff();
};

#endif /* RGBLED_HPP */