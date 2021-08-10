import serial
import sys

class Serial:
    def __init__(self, port):
        self.serial_port= serial_port
        try:
            self.serial_con = serial.Serial(self.serial_port, 9600)
        except:
            print(f"Error: Could not open serial port {self.serial_port}")
            sys.exit(1)

    def close(self):
        self.serial_port.close()

    def send_command(self, command):
        self.serial_con.write(command.encode())
