#!/usr/bin/env python3

import serial
import sys
import binascii

class Lidar:
    def __init__(self, port='/dev/ttyUSB0'):
        self.baudrate = 230400
        self.port = port
        self.serial_con = serial.Serial(self.port, self.baudrate)

    def _send(self, arr):
        self.serial_con.write(arr)

    def start(self):
        values = bytearray([0xA5, 0x60])
        self._send(values)

    def stop(self):
        values = bytearray([0xA5, 0x65])
        self._send(values)

    def read(self):
        b = self.serial_con.read(8)
        b = binascii.hexlify(bytearray(b))
        print(b)

        for i in range(180):
            b = self.serial_con.read(14)
            b = binascii.hexlify(bytearray(b))
            print(b)

def main(argc, argv):
    if argc == 2:
        l = Lidar(sys.argv[1])
    else :
        l = Lidar
    l.start()
    l.read()
    l.stop()

if __name__ == "__main__":
    main(len(sys.argv), sys.argv)
