import sys
import time
import socket
from values import *


class Hexapod:
    def __init__(self, host, port):
        self.socket = socket.socket()
        self.host = host
        self.port = port

    def __exit__(self, type, value, traceback):
        self.socket.close()

    def __enter__(self):
        return
        self.socket.connect((self.host, self.port))

    def wait_interrupt(self, message="waiting"):
        try:
            print(message, file=sys.stderr)
            while True:
                time.sleep(2)
        except KeyboardInterrupt:
            return

    def __move_engine(self, articulation, deg, tab, sleep):
        if (articulation > 15):
            deg = deg * (tab[0][0] - tab[0][1]) + tab[0][1]
        else:
            deg = deg * (tab[1][0] - tab[1][1]) + tab[1][1]
        line = "#%dP%.0fS700!" % (articulation, deg)
        command = bytes(line.encode('utf-8'))
        # self.socket.send(command)
        print(command)
        time.sleep(sleep)

    def move_knee(self, articulation, deg, sleep):
        self.__move_engine(articulation, deg, KNEE_VALUES, sleep)

    def move_vert(self, articulation, deg, sleep):
        self.__move_engine(articulation, deg, VERT_VALUES, sleep)

    def move_hori(self, articulation, deg, sleep):
        self.__move_engine(articulation, deg, HORI_VALUES, sleep)


# DEPRECATED
# INPUT = "/dev/ttyUSB0"
# def open_usb(input):
#     try:
#         sys.stdout = open(input, "w")
#     except (PermissionError) as error:
#         print("Could not find hexapod input: %s" % error)
#         # print("try \n\033[1m\033[31msudo chmod 777 %s\033[0m" % input)
#         import os
#         os.system("sudo chmod 777 %s" % input)
#         exit(1)
# open_usb(INPUT)
