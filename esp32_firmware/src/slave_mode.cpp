#include "slave_mode.hpp"
#include "HardwareSerial.h"

SlaveMode::SlaveMode(HexapodSerialController &hexapodSerialController) :
    _hexapodSerialController(hexapodSerialController)
{
}

void SlaveMode::setup()
{
    _SerialBT.begin("HexaPoC");
}

void SlaveMode::loop()
{
    if (_SerialBT.available()) {
        // Serial.write(_SerialBT.read());
        _hexapodSerialController.send(_SerialBT.read());

    }
}