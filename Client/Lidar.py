import serial
import sys

values = bytearray([0xA5, 0x65])
ser.write(values)

class Lidar:
    def __init__(self, port='/dev/ttyUSB0'):
        self.baudrate = 230400
        self.port = '/dev/ttyUSB0'
        self.serial_con = serial.Serial(self.port, self.baudrate)

    def _send(arr):
        self.serial_con.write(arr)

    def start():
        values = bytearray([0xA5, 0x60])
        self.send(values)

    def stop():
        values = bytearray([0xA5, 0x65])
        self.send(values)

    def read():
        pass

def main(argc, argv):
    l = Lidar
    l.start()
    l.read()
    l.stop()

if __name__ == "__main__":
    main(len(sys.argv), sys.argv)