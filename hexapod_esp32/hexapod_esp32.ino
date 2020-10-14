#include "BluetoothSerial.h"
#include "Ultrasound.hpp"

#include <SoftwareSerial.h>

const byte TRIGGER_PIN = 13;
const byte ECHO_PIN = 12;

Ultrasound UltrasoundModule(TRIGGER_PIN, ECHO_PIN);
SoftwareSerial port(2, 15);
BluetoothSerial SerialBT;

void setup()
{
    Serial.begin(115200);
    port.begin(9600);
    SerialBT.begin("ESP32_Hexapod");
}

void loop()
{
    if (SerialBT.available()) {
        port.write(SerialBT.read());
    }
    delay(20);
}
