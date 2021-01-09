#ifndef SLAVE_MODE_HPP
#define SLAVE_MODE_HPP

#include "BluetoothSerial.h"
#include "HexapodSerialController.hpp"

class SlaveMode {
    private:
        BluetoothSerial _SerialBT;
        HexapodSerialController &_hexapodSerialController;

    public:
        SlaveMode(HexapodSerialController &hexapodSerialController);
        void setup();
        void loop();
};

#endif /* SLAVE_MODE_HPP */