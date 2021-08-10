#ifndef SLAVE_MODE_HPP
#define SLAVE_MODE_HPP

#include "HexapodSerialController.hpp"

#include <string>

class SlaveMode {
  private:
    HexapodSerialController &_hexapodSerialController;
    void bleRxCallback(std::string str);

  public:
    SlaveMode(HexapodSerialController &hexapodSerialController);
    void setup();
    void loop();
};

#endif /* SLAVE_MODE_HPP */