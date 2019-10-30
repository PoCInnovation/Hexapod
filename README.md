# DISCLAIMER : README IS NOT UP TO DATE AT ALL, DON'T REFER TO IT, I WILL UPDATE IT WHEN I'LL HAVE THE TIME
# Hexapod

See `DEMO` for quick use.

## Start the Hexapod

- Plug the battery to the robot.

## Connect the Hexapod

#### Flash and power the ESP-32
- Flash the arduino code from `./Arduino_Code` to the ESP-32.
- Connect `VS2+` from the Hexapod to `VIN` on the ESP-32.
- Connect `VS2-` from the Hexapod to `GND` on the ESP-32.

#### Connect the Hexapod to the ESP-32
- Connect `TX` from the Hexapod to `D2` on the ESP-32.
- Connect `RX` from the Hexapod to `D15` on the ESP-32.
- Connect `G` from the Hexapod to `GND` on the ESP-32.

#### Connect to the Hexapod
- Connect your computer to the wifi `hexapod_wifi`.


# Control

Control the robotic with Hexapod class in ./Python/movements/hexapod.py.<br />
Create a class instance and use the class methods to move the engines.

See `DEMO` for exemples.

# Demo

A demo can be found in `./Python/movements/demoMain.py`.

It creates a class instance of Hexapod and HexapodDemo.

HexapodDemo is a class from `./Python/movements/demoCode.py`<br />
It contains wrapper for the Hexapod class, like `stand`, `sit`, `wait`, `wave` and `dab`

The main connects to the Hexapod and tells it to stand, wave, dab, and sit.<br />
After each actions, it stops the Hexapod and waits for a `SIGINT` from the terminal.

## Launch Demo
- Follow instructions from `Hexapod - Start the Hexapod`<br />
/!\ The ESP-32 from PoC is already flashed!<br />
`You only need to plug the wires, switch the battery lever and connect to wifi.`

- Launch the `demoMain.py` script.

- The Hexapod will stand, wave and dab.<br />
Remember, the Hexapod waits for you to tell it when to stop an action.

- The Hexapod will sit and the script will end.

- The demo is done and ready for another use.


# Notes

- For any assistance, feel free to ask `lorenzo.rosmarino@epitech.eu` or `yohann.assouline@epitech.eu`

- ### `/!\ Remember to charge the batteries`
