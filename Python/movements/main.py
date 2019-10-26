#!/usr/bin/python3

import socket
import sys
import time
from values import *

SOCKET_HOST = "192.168.4.1"  # ESP32 IP in local network
SOCKET_PORT = 80             # ESP32 Server Port

class Hexapod_movements:
    def __init__(self, connection):
        self.hexapod_connection = connection

    def move_engine(self, articulation, deg, speed, tab, sleep_time):
        # We need to know which side the engine is on
        side = articulation <= 15
        # Convert ratio 0-1 to the engine min-max value
        deg = deg * (tab[side][0] - tab[side][1]) + tab[side][1]
        # Command to send to the LynxMotion board
        line = "#%dP%.0fS%d!" % (articulation, deg, speed)
        # #=pin
        # P=position
        # S=speed
        # !=custom EOL for arduino decode
        self.hexapod_connection.send_command(line, sleep_time)

    def move_knee(self, articulation, deg, sleep):
        self.move_engine(articulation, deg, 700, KNEE_VALUES, sleep)

    def move_vert(self, articulation, deg, sleep):
        self.move_engine(articulation, deg, 700, VERT_VALUES, sleep)

    def move_hori(self, articulation, deg, sleep):
        self.move_engine(articulation, deg, 700, HORI_VALUES, sleep)

class HexapodConnection:
    def __init__(self, host, port):
        self.socket = socket.socket()
        self.host = host
        self.port = port
        self.init_connection()

    def __exit__(self, type, value, traceback):
        self.socket.close()

    def init_connection(self):
        try:
            self.socket.connect((self.host, self.port))
        except:
            print("You must connect to Hexapod's wifi first")
            exit(1)

    def send_command(command, sleep_time):
        command = bytes(line.encode('utf-8'))
        self.socket.send(command)
        # print(command) # <-- DEBUG
        time.sleep(sleep_time)


class Hexapod:
    def __init__(self):
        self.connection = HexapodConnection(SOCKET_HOST, SOCKET_PORT)
        # self.connection = 1 # debug
        self.hexapod_movements = Hexapod_movements(self.connection)
        self.valid_commands = ["help", "sit", "stand", "forward"]
        self.start_prompt()

    def print_help(self):
        print("Available commands :")
        for command in self.valid_commands:
            print(command, end='\t')
        print("\n")

    def start_prompt(self):
        print("Type help to see available commands")
        while True:
            try:
                command = input("$ ")
            except:
                exit(0)
            if command not in self.valid_commands:
                print("{} : Invalid command".format(command))
                continue

            if command == "help":
                self.print_help()
            else:
                self.do_action(command)

    def do_action(self, command):
        print("Command:", command) # debug
        if command == "sit":
            pass
        elif command == "forward":
            pass
        elif command == "stand":
            pass

if __name__ == '__main__':
    Hexapod()
