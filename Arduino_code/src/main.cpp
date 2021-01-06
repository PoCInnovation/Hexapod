#include "BluetoothSerial.h"

#include <Arduino.h>

BluetoothSerial SerialBT;

void setup()
{
    Serial.begin(115200);

    SerialBT.begin("HexaPoC");
}

void loop()
{
    if (Serial.available()) {
        SerialBT.write(Serial.read());
    }
    if (SerialBT.available()) {
        Serial.write(SerialBT.read());
    }
    delay(20);
}
