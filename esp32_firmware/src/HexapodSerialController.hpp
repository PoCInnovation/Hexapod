#ifndef HEXAPODSERIALCONTROLLER_HPP
#define HEXAPODSERIALCONTROLLER_HPP

#include "HardwareSerial.h"

class HexapodSerialController {
  private:
    /* data */
    HardwareSerial _mySerial;

  public:
    HexapodSerialController(/* args */);
    void send(char *buff);
    // void send(int byte);
    // void read();
};

#endif /* HEXAPODSERIALCONTROLLER_HPP */