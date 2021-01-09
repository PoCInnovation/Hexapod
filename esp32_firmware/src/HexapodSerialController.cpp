#include "HexapodSerialController.hpp"

HexapodSerialController::HexapodSerialController() : _mySerial(1)
{
    _mySerial.begin(9600);
}

void HexapodSerialController::send(char *buff)
{
    while (!_mySerial.availableForWrite()) {
        ;
    }
    _mySerial.write(buff);
}

void HexapodSerialController::send(int byte)
{
    while (!_mySerial.availableForWrite()) {
        ;
    }
    _mySerial.write(byte);
}
