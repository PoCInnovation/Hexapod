import time
import socket
from values import *

# Hexapod Class
# Receives the host and the port of the physical Hexapod to create a socket
# Use it in a `with hexapod:` statement block
#           (automaticaly connects and disconnects the socket)


class Hexapod:
    def __init__(self, host, port):
        self.socket = socket.socket()
        self.host = host
        self.port = port

    def __exit__(self, type, value, traceback):
        self.socket.close()

    def __enter__(self):
        # return
        self.socket.connect((self.host, self.port))

    # Sends movements to the Hexapod
    # Do not call it yourself, use the following move_* functions
    # articulation = engine pin
    # deg = ratio of min-max (0 - 1)
    def __move_engine(self, articulation, deg, speed, tab, sleep):

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

        # We need to encode the command to send it via sockets
        command = bytes(line.encode('utf-8'))

        # We send the command via WiFi
        self.socket.send(command)
        # print(command)

        # Finally, we can add some sleep to avoid flooding the board
        time.sleep(sleep)

    def move_knee(self, articulation, deg, sleep):
        self.__move_engine(articulation, deg, 700, KNEE_VALUES, sleep)

    def move_vert(self, articulation, deg, sleep):
        self.__move_engine(articulation, deg, 700, VERT_VALUES, sleep)

    def move_hori(self, articulation, deg, sleep):
        self.__move_engine(articulation, deg, 700, HORI_VALUES, sleep)
