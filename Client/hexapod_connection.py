import time
import serial
import socket
import os
from values import *

SOCKET_HOST = "192.168.4.1"  # ESP32 IP in local network
SOCKET_PORT = 80             # ESP32 Server Port

class HexapodConnection:
    """
    Class helping with hardware communication
    Compatible with wired/wireless
    """

    def __init__(self, serial_port):
        self.serial_port= serial_port

        if self.serial_port == None:
            self.socket = socket.socket()
            self.host = SOCKET_HOST
            self.socket_port = SOCKET_PORT
            self.init_connection()
        else:
            self.serial_con = serial.Serial(self.serial_port, 9600)

    def init_connection(self):
        print("Connecting...")
        try:
            self.socket.connect((self.host, self.socket_port))
        except:
            print("\nYou must connect to Hexapod's wifi first")
            exit(1)

    def close(self):
        if self.serial_port == None:
            self.socket.close()

    def send_command(self, command, sleep_time=0):
        if self.serial_port == None:
            print(command)
            command = bytes(command.encode('utf-8'))
            try:
                self.socket.send(command)
            except:
                print("\nError : couldn't send command")
                self.close()
                exit(1)
        else:
            command.replace('!', '')
            # self.serial_con.write(command.encode())
            # print(command)
            # print(command.encode())
            t = 'echo "' + command + '" > /dev/tty.usbserial-AK06II1T'
            os.system(t)
        # print("sending : ", command)
        # time.sleep(sleep_time)
