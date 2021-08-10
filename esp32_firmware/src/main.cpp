#include "HexapodSerialController.hpp"
#include "autonomous_mode.hpp"
#include "ble_con.hpp"
#include "remote_controlled_mode.hpp"
#include "rgbled.hpp"
#include "slave_mode.hpp"

#include <Arduino.h>

HexapodSerialController hexapodSerialController;
SlaveMode slaveMode(hexapodSerialController);
RemoteControlledMode remoteControlledMode(hexapodSerialController);
AutonomousMode autonomousMode(hexapodSerialController);

RGBled led(33, 25, 32);

typedef enum {
    SLAVE,
    REMOTE_CONTROLLED,
    AUTONOMOUS,
} firmware_mode_e;
firmware_mode_e firmware_mode;

const uint8_t PIN_MODE_SELECTOR_1 = 34;
const uint8_t PIN_MODE_SELECTOR_2 = 35;

void setup()
{
    Serial.begin(115200);

    pinMode(PIN_MODE_SELECTOR_1, INPUT_PULLUP);
    pinMode(PIN_MODE_SELECTOR_2, INPUT_PULLUP);

    // const uint8_t state1 = !digitalRead(PIN_MODE_SELECTOR_1);
    // const uint8_t state2 = !digitalRead(PIN_MODE_SELECTOR_2);

    const uint8_t state1 = true;
    const uint8_t state2 = false;

    Serial.println(state1);
    Serial.println(state2);

    BleCon::init();

    if (state1 && !state2) {
        Serial.println("Slave mode");
        firmware_mode = SLAVE;
        led.setColor(RGB_RED);
        slaveMode.setup();
    } else if (state2 && !state1) {
        Serial.println("Remote mode");
        firmware_mode = REMOTE_CONTROLLED;
        led.setColor(RGB_GREEN);
        remoteControlledMode.setup();
    } else {  // !state1 && !state2
        Serial.println("Automomous mode");
        firmware_mode = AUTONOMOUS;
        led.setColor(RGB_BLUE);
        autonomousMode.setup();
    }
}

void loop()
{
    switch (firmware_mode) {
        case SLAVE:
            slaveMode.loop();
            break;
        case REMOTE_CONTROLLED:
            remoteControlledMode.loop();
            break;
        case AUTONOMOUS:
            autonomousMode.loop();
            break;
    }
}