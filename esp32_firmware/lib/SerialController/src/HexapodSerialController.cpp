#include "HexapodSerialController.hpp"

HexapodSerialController::HexapodSerialController(int uart_nb) : _mySerial(uart_nb)
{
    _mySerial.begin(9600);
}

void HexapodSerialController::send(const char *buff)
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