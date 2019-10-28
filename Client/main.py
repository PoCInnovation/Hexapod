#!/usr/bin/python3

import time
from values import *
from hardcoded_movements import *
from hexapod_connection import*

class Hexapod:
    def __init__(self):
        self.connection = HexapodConnection()
        self.hexapod_movements = HardcodedMovements(self.connection)
        self.valid_commands = ["help", "sit", "stand", "forward", "dab", "wave", "stand1", "stand2", "stand3"]
        self.position = "sit"
        self.start_prompt()

    def print_help(self):
        print("Available commands :")
        for command in self.valid_commands:
            print(" ", command)
        print("\n")

    def check_command_possibility(self, command):
        initial_position = self.position
        if self.position == "sit":
            if command == "stand":
                self.position = "stand"
            elif command == "dab" or command == "wave":
                self.do_action("stand")
                time.sleep(1)
        elif self.position == "stand":
            if command == "sit":
                self.position = "sit"
        self.do_action(command)
        if self.position != initial_position:
            if initial_position == "sit" and command != "stand":
                self.do_action("sit")

    def start_prompt(self):
        print("Type help to see available commands")
        print("You should always start with the 'sit' command")
        while True:
            try:
                command = input("$ ")
            except:
                self.connection.close()
                exit(0)
            if command not in self.valid_commands:
                print("{} : Invalid command".format(command))
                continue

            if command == "help":
                self.print_help()
            else:
                self.check_command_possibility(command)

    def do_action(self, command):
        print("Command:", command)
        getattr(self.hexapod_movements, command)()

if __name__ == '__main__':
    Hexapod()
