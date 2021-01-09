#ifndef REMOTE_CONTROLLED_MODE_HPP
#define REMOTE_CONTROLLED_MODE_HPP

#include "HexapodSerialController.hpp"

class RemoteControlledMode
{
private:
    HexapodSerialController &_hexapodSerialController;

public:
    RemoteControlledMode(HexapodSerialController &hexapodSerialController);
    void setup();
    void loop();
};

#endif /* REMOTE_CONTROLLED_MODE_HPP */