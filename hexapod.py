#!/bin/python3

import sys
from values import *
from engine_mouvements import *

INPUT = "/dev/ttyUSB0"

def open_usb(input):
    try:
        sys.stdout = open(input, "w")
    except (PermissionError) as error:
        print("Could not find hexapod input: %s" % error)
        # print("try \n\033[1m\033[31msudo chmod 777 %s\033[0m" % input)
        import os
        os.system("sudo chmod 777 %s" % input)
        exit(1)

def demo_sit():
    move_vert(FRON_L_VERT, 1, 0)
    move_vert(FRON_R_VERT, 1, 0.25)
    move_vert(REAR_L_VERT, 1, 0)
    move_vert(REAR_R_VERT, 1, 0.25)
    move_vert(MIDD_L_VERT, 1, 0)
    move_vert(MIDD_R_VERT, 1, 0.25)

    move_knee(FRON_L_KNEE, 0, 0)
    move_knee(FRON_R_KNEE, 0, 0.25)
    move_knee(REAR_L_KNEE, 0, 0)
    move_knee(REAR_R_KNEE, 0, 0.25)
    move_knee(MIDD_L_KNEE, 0, 0)
    move_knee(MIDD_R_KNEE, 0, 1)

    move_hori(FRON_L_HORI, 0.5, 0)
    move_hori(FRON_R_HORI, 0.5, 0.25)
    move_hori(REAR_L_HORI, 0.5, 0)
    move_hori(REAR_R_HORI, 0.5, 0.25)
    move_hori(MIDD_L_HORI, 0.5, 0)
    move_hori(MIDD_R_HORI, 0.5, 0.25)

def demo_stand():
    move_knee(FRON_L_KNEE, 0.3, 0)
    move_knee(FRON_R_KNEE, 0.3, 0.25)
    move_knee(REAR_L_KNEE, 0.3, 0)
    move_knee(REAR_R_KNEE, 0.3, 0.25)
    move_knee(MIDD_L_KNEE, 0.3, 0)
    move_knee(MIDD_R_KNEE, 0.3, 0.25)

    move_vert(MIDD_L_VERT, 0.4, 0)
    move_vert(MIDD_R_VERT, 0.4, 0.25)
    move_vert(REAR_L_VERT, 0.4, 0)
    move_vert(REAR_R_VERT, 0.4, 0.25)
    move_vert(FRON_L_VERT, 0.4, 0)
    move_vert(FRON_R_VERT, 0.4, 0.25)

    move_knee(FRON_L_KNEE, 0.5, 0)
    move_knee(FRON_R_KNEE, 0.5, 0.25)
    move_knee(REAR_L_KNEE, 0.5, 0)
    move_knee(REAR_R_KNEE, 0.5, 0.25)
    move_knee(MIDD_L_KNEE, 0.5, 0)
    move_knee(MIDD_R_KNEE, 0.5, 0.25)

open_usb(INPUT)
demo_sit()
# sys.exit(0)
demo_stand()
