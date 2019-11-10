import time
import socket
import os

SOCKET_HOST = "192.168.4.1"  # ESP32 IP in local network
SOCKET_PORT = 80             # ESP32 Server Port

class HexapodConnection:
    def __init__(self, host=SOCKET_HOST, port=SOCKET_PORT, mode="wifi"):
        self.mode = mode
        if self.mode == "wifi":
            self.socket = socket.socket()
            self.host = host
            self.port = port
            self.init_connection()


    def close(self):
        if self.mode == "wifi":
            self.socket.close()

    def init_connection(self):
        print("Connecting...")
        try:
            self.socket.connect((self.host, self.port))
        except:
            print("\nYou must connect to Hexapod's wifi first")
            exit(1)

    def send_command(self, command, sleep_time):
        if self.mode == "wifi":
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
            t = 'echo "' + command + '" > /dev/ttyUSB0'
            os.system(t)
        # print(command)
        time.sleep(sleep_time)
