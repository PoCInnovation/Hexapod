from values import *
import time
import socket

sock = socket.socket()
host = "192.168.4.1"  #ESP32 IP in local network
port = 80             #ESP32 Server Port
sock.connect((host, port))

def move_engine(leg, deg):
    line = "#%dP%.0fS700!" % (leg, deg)
    command = bytes(line.encode('utf-8'))
    sock.send(command)

def move_knee(leg, deg, sleep):
    if (leg > 15):
        deg = deg * (MAX_L_KNEE - MIN_L_KNEE) + MIN_L_KNEE
    else:
        deg = deg * (MAX_R_KNEE - MIN_R_KNEE) + MIN_R_KNEE
    move_engine(leg, deg)
    time.sleep(sleep)

def move_vert(leg, deg, sleep):
    if (leg > 15):
        deg = deg * (MAX_L_VERT - MIN_L_VERT) + MIN_L_VERT
    else:
        deg = deg * (MAX_R_VERT - MIN_R_VERT) + MIN_R_VERT
    move_engine(leg, deg)
    time.sleep(sleep)

def move_hori(leg, deg, sleep):
    if (leg > 15):
        deg = deg * (MAX_L_HORI - MIN_L_HORI) + MIN_L_HORI
    else:
        deg = deg * (MAX_R_HORI - MIN_R_HORI) + MIN_R_HORI
    move_engine(leg, deg)
    time.sleep(sleep)
