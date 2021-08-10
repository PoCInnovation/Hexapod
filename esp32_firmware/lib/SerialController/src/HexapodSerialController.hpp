#ifndef HEXAPODSERIALCONTROLLER_HPP
#define HEXAPODSERIALCONTROLLER_HPP

#include "HardwareSerial.h"

class HexapodSerialController {
  private:
    HardwareSerial _mySerial;

  public:
    HexapodSerialController(int uart_nb);
    void send(const char *buff);
    void send(int byte);
    // void read();
};

#endif /* HEXAPODSERIALCONTROLLER_HPP */