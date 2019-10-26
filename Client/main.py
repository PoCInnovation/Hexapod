#!/usr/bin/python3

import socket
import sys
import time
from values import *
from hardcoded_movements import *

SOCKET_HOST = "192.168.4.1"  # ESP32 IP in local network
SOCKET_PORT = 80             # ESP32 Server Port

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

    def send_command(self, command, sleep_time):
        command = bytes(command.encode('utf-8'))
        self.socket.send(command)
        time.sleep(sleep_time)


class Hexapod:
    def __init__(self):
        self.connection = HexapodConnection(SOCKET_HOST, SOCKET_PORT)
        # self.connection = 1 # debug
        self.hexapod_movements = HardcodedMovements(self.connection)
        self.valid_commands = ["help", "sit", "stand", "forward", "dab", "wave"]
        self.position = "sit"
        self.start_prompt()

    def print_help(self):
        print("Available commands :")
        for command in self.valid_commands:
            print(" ", command)
        print("\n")

    def check_command_possibility(self, command):
        if self.position == "sit":
            if command == "stand":
                self.position = "stand"
            elif command == "dab" or command == "wave" or command == "forward":
                self.do_action("stand")
                time.sleep(1)
                self.position = "stand"
        if self.position == "stand":
            if command == "sit":
                self.position = "sit"
        self.do_action(command)



    def start_prompt(self):
        print("Type help to see available commands")
        print("You should always start with the 'sit' command")
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
                self.check_command_possibility(command)

    def do_action(self, command):
        print("Command:", command) # debug
        getattr(self.hexapod_movements, command)()

if __name__ == '__main__':
    Hexapod()
