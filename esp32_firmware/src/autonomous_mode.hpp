#ifndef AUTONOMOUS_MODE_HPP
#define AUTONOMOUS_MODE_HPP

#include "HexapodSerialController.hpp"

class AutonomousMode {
  private:
    HexapodSerialController &_hexapodSerialController;

  public:
    AutonomousMode(HexapodSerialController &hexapodSerialController);
    void setup();
    void loop();
};

#endif /* AUTONOMOUS_MODE_HPP */