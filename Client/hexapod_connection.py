import time
import socket
import os
from values import *

SOCKET_HOST = "192.168.4.1"  # ESP32 IP in local network
SOCKET_PORT = 80             # ESP32 Server Port

ENGINES_POSITION = {
    VERT_REAR_R   : 0,
    HORI_REAR_R   : 0,
    VERT_MIDDLE_R : 0,
    HORI_MIDDLE_R : 0,
    VERT_FRONT_R  : 0,
    HORI_FRONT_R  : 0,
    KNEE_REAR_R   : 0,
    KNEE_MIDDLE_R : 0,
    KNEE_FRONT_R  : 0,
    VERT_REAR_L   : 0,
    HORI_REAR_L   : 0,
    VERT_MIDDLE_L : 0,
    HORI_MIDDLE_L : 0,
    VERT_FRONT_L  : 0,
    HORI_FRONT_L  : 0,
    KNEE_REAR_L   : 0,
    KNEE_MIDDLE_L : 0,
    KNEE_FRONT_L  : 0
}


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

    def save_engine_position(self, command):
        global ENGINES_POSITION
        ''' This should always work with the gui but if you use tester.py
        and make a mistake this try/except will prevent from crashing '''
        try:
            commands_array = command.split('#')
        except:
            print('could not split : ', command)
            return

        for com in commands_array:
            if len(com) == 0:
                continue
            try:
                engine = int(com[0:com.index('P')])
                position = int(com[com.index('P') + 1:com.index('S')])
                print("Save : ", command, engine , position)
                ENGINES_POSITION[engine] = position
            except:
                print("Could not save engine position with the command", com)
                continue

    def get_engine_position(self, engine):
        if type(engine) == str:
            if engine == 'all':
                return ENGINES_POSITION
        elif type(engine) == int:
            return ENGINES_POSITION[engine]

    def send_command(self, command, sleep_time=0):
        if self.mode == "wifi":
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
        # print("sending : ", command)
        self.save_engine_position(command)
        # time.sleep(sleep_time)
