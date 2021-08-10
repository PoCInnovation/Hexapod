#include "slave_mode.hpp"

#include "HardwareSerial.h"
#include "ble_con.hpp"

#include <functional>
#include <string>

SlaveMode::SlaveMode(HexapodSerialController &hexapodSerialController) :
    _hexapodSerialController(hexapodSerialController)
{
}

void SlaveMode::bleRxCallback(std::string str)
{
    Serial.println("Received in cb:");
    Serial.println(str.c_str());
    Serial.println();
    Serial.println("OIK");
}

void SlaveMode::setup()
{
    std::function<void(std::string)> f = std::bind(&SlaveMode::bleRxCallback, this, std::placeholders::_1);
    BleCon::setCallback(f);
}

void SlaveMode::loop()
{
    BleCon::updateEvents();
}