#!/bin/python3

import time
import sys
from values import *

INPUT = "/dev/ttyUSB0"

try:
    sys.stdout = open(INPUT, "w")
except (PermissionError) as error:
    print("Could not find hexapod input: %s" % error)
    # print("try \n\033[1m\033[31msudo chmod 777 %s\033[0m" % INPUT)
    import os
    os.system("sudo chmod 777 %s" % INPUT)
    exit(1)

def move_engine(leg, deg):
    command = "#%dP%.0f" % (leg, deg)
    print(command)

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

move_knee(FRON_L_KNEE, 0.5, 0)
move_knee(FRON_R_KNEE, 0.5, 0.25)
move_knee(REAR_L_KNEE, 0.5, 0)
move_knee(REAR_R_KNEE, 0.5, 0.25)
move_knee(MIDD_L_KNEE, 0.5, 0)
move_knee(MIDD_R_KNEE, 0.5, 0.25)

move_hori(FRON_L_HORI, 0.5, 0)
move_hori(FRON_R_HORI, 0.5, 0.25)
move_hori(REAR_L_HORI, 0.5, 0)
move_hori(REAR_R_HORI, 0.5, 0.25)
move_hori(MIDD_L_HORI, 0.5, 0)
move_hori(MIDD_R_HORI, 0.5, 0.25)

move_vert(FRON_L_VERT, 0.3, 0)
move_vert(FRON_R_VERT, 0.3, 0.25)
move_vert(REAR_L_VERT, 0.3, 0)
move_vert(REAR_R_VERT, 0.3, 0.25)
move_vert(MIDD_L_VERT, 0.3, 0)
move_vert(MIDD_R_VERT, 0.3, 0.25)

# move_vert(MIDD_R_VERT, 0.4, 0.25)
# move_knee(MIDD_R_KNEE, 0.5, 0.25)
# move_vert(MIDD_R_VERT, 0.3, 0.25)
