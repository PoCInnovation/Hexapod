#include "remote_controlled_mode.hpp"

#include "ble_con.hpp"

#include <functional>

RemoteControlledMode::RemoteControlledMode(HexapodSerialController &hexapodSerialController) :
    _hexapodSerialController(hexapodSerialController)
{
}

/*
    Available commands are :

        F -> Forward (until stop)
        B -> Backward (until stop)
        R -> Right (until stop)
        L -> Left (until stop)
        S -> Stop

        TR -> Turn right
        TL -> Turn left

        U1 -> Up position 1
        U2 -> Up position 2
        U3 -> Up position 3

        RST -> Reset position

        HI -> Say hi with a leg
        DAB -> Do a dab

        SIT -> Sit down and turn motors off
*/

void RemoteControlledMode::bleRxCallback(std::string str)
{
    if (str.size() == 1) {
        switch (str[0]) {
            case 'F':
                // TODO
                break;

            case 'B':
                // TODO
                break;

            case 'R':
                // TODO
                break;

            case 'L':
                // TODO
                break;

            case 'S':
                // TODO
                break;
        }
    } else if (str[0] == 'T') {  // turn
        if (str[1] == 'R') {
            // TODO
        } else if (str[1] == 'L') {
            // TODO
        }
    } else if (str[0] == 'U') {
        // TODO
    } else if (str == "RST") {
        // TODO
    } else if (str == "HI") {
        // TODO
    } else if (str == "DAB") {
        // TODO
    } else if (str == "SIT") {
        // TODO
    }
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