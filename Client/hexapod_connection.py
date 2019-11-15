import time
import socket
import os
from values import *

SOCKET_HOST = "192.168.4.1"  # ESP32 IP in local network
SOCKET_PORT = 80             # ESP32 Server Port

ENGINES_POSITION = {
    REAR_R_HORI: 0,
    REAR_R_VERT: 0,
    REAR_R_KNEE: 0,
    REAR_L_HORI: 0,
    REAR_L_VERT: 0,
    REAR_L_KNEE: 0,
    MIDD_R_HORI: 0,
    MIDD_R_VERT: 0,
    MIDD_R_KNEE: 0,
    MIDD_L_HORI: 0,
    MIDD_L_VERT: 0,
    MIDD_L_KNEE: 0,
    FRON_R_HORI: 0,
    FRON_R_VERT: 0,
    FRON_R_KNEE: 0,
    FRON_L_HORI: 0,
    FRON_L_VERT: 0,
    FRON_L_KNEE: 0
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
            engine = int(command[1:command.index('P')])
            position = int(command[command.index('P') + 1:command.index('S')])
        except:
            print("Could not save engine position with the command", command)
            return
        ENGINES_POSITION[engine] = position

    def get_engine_position(self, engine):
        if type(engine) == str:
            if engine == 'all':
                return ENGINES_POSITION
        elif type(engine) == int:
            return ENGINES_POSITION[engine]

    def convert_angle(self, angle, engine, kind):
        side = engine <= 15   # We need to know which side the engine is on
        if kind == "v":
            vals = VERT_VALUES
        elif kind == "h":
            vals = HORI_VALUES
        else:  # k
            vals = KNEE_VALUES
        return angle * (vals[side][0] - vals[side][1]) + vals[side][1]

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
        #  print(command)
        self.save_engine_position(command)
        time.sleep(sleep_time)
