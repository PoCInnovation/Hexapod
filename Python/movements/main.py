#!/bin/python3
from hexapod import Hexapod
from demo import HexapodDemo

SOCKET_HOST = "192.168.4.1"  # ESP32 IP in local network
SOCKET_PORT = 80             # ESP32 Server Port

hexapod = Hexapod(SOCKET_HOST, SOCKET_PORT)

if __name__ == '__main__':
    with hexapod:
        demo_hexapod = HexapodDemo(hexapod)
        demo_hexapod.demo_sit(0, 0)
        demo_hexapod.demo_stand(0.25, 1)
        demo_hexapod.wait_interrupt()

        demo_hexapod.demo_wave(0.5, 2)
        demo_hexapod.wait_interrupt()

        demo_hexapod.demo_dab(0.25, 1)
        demo_hexapod.wait_interrupt()

        demo_hexapod.demo_sit(0, 0)
