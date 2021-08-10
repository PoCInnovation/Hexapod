#include "remote_controlled_mode.hpp"

#include "ble_con.hpp"

#include <functional>

RemoteControlledMode::RemoteControlledMode(HexapodSerialController &hexapodSerialController) :
    _hexapodSerialController(hexapodSerialController)
{
}

void RemoteControlledMode::bleRxCallback(std::string str)
{
    Serial.println("Received in cb:");
    Serial.println(str.c_str());
    Serial.println();
    Serial.println("OIK");
    // _hexapodSerialController.send(str.c_str());
}

void RemoteControlledMode::setup()
{
    std::function<void(std::string)> f = std::bind(&RemoteControlledMode::bleRxCallback, this, std::placeholders::_1);
    BleCon::setCallback(f);
}

void RemoteControlledMode::loop()
{
    BleCon::updateEvents();
}