#ifndef REMOTE_CONTROLLED_MODE_HPP
#define REMOTE_CONTROLLED_MODE_HPP

#include "HexapodSerialController.hpp"

#include <string>

class RemoteControlledMode {
  private:
    HexapodSerialController &_hexapodSerialController;
    void bleRxCallback(std::string str);

  public:
    RemoteControlledMode(HexapodSerialController &hexapodSerialController);
    void setup();
    void loop();
};

#endif /* REMOTE_CONTROLLED_MODE_HPP */