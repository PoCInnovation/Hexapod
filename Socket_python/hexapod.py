#!/bin/python3

import sys
from values import *
from engine_mouvements import *

INPUT = "/dev/ttyUSB0"

# def open_usb(input):
# return
#     try:
#         sys.stdout = open(input, "w")
#     except (PermissionError) as error:
#         print("Could not find hexapod input: %s" % error)
#         # print("try \n\033[1m\033[31msudo chmod 777 %s\033[0m" % input)
#         import os
#         os.system("sudo chmod 777 %s" % input)
#         exit(1)

def wait_interrupt():
    try:
        while True:
            print(".", file=sys.stderr)
            time.sleep(0.5)
    except KeyboardInterrupt:
        return

def demo_sit(sleep_action, sleep_timing):
    move_vert(FRON_L_VERT, 1, 0)
    move_vert(FRON_R_VERT, 1, sleep_action)
    move_vert(REAR_L_VERT, 1, 0)
    move_vert(REAR_R_VERT, 1, sleep_action)
    move_vert(MIDD_L_VERT, 1, 0)
    move_vert(MIDD_R_VERT, 1, sleep_action)

    move_knee(FRON_L_KNEE, 0, 0)
    move_knee(FRON_R_KNEE, 0, sleep_action)
    move_knee(REAR_L_KNEE, 0, 0)
    move_knee(REAR_R_KNEE, 0, sleep_action)
    move_knee(MIDD_L_KNEE, 0, 0)
    move_knee(MIDD_R_KNEE, 0, 1)

    move_hori(FRON_L_HORI, 0.5, 0)
    move_hori(FRON_R_HORI, 0.5, sleep_action)
    move_hori(REAR_L_HORI, 0.5, 0)
    move_hori(REAR_R_HORI, 0.5, sleep_action)
    move_hori(MIDD_L_HORI, 0.5, 0)
    move_hori(MIDD_R_HORI, 0.5, sleep_timing)

def demo_stand(sleep_action, sleep_timing):
    move_hori(FRON_L_HORI, 0.5, 0)
    move_hori(FRON_R_HORI, 0.5, 0)
    move_hori(REAR_L_HORI, 0.5, 0)
    move_hori(REAR_R_HORI, 0.5, 0)
    move_hori(MIDD_L_HORI, 0.5, 0)
    move_hori(MIDD_R_HORI, 0.5, 0)

    move_knee(FRON_L_KNEE, 0.3, 0)
    move_knee(FRON_R_KNEE, 0.3, sleep_action)
    move_knee(REAR_L_KNEE, 0.3, 0)
    move_knee(REAR_R_KNEE, 0.3, sleep_action)
    move_knee(MIDD_L_KNEE, 0.3, 0)
    move_knee(MIDD_R_KNEE, 0.3, sleep_action)

    move_vert(MIDD_L_VERT, 0.4, 0)
    move_vert(MIDD_R_VERT, 0.4, sleep_action)
    move_vert(FRON_L_VERT, 0.4, 0)
    move_vert(FRON_R_VERT, 0.4, sleep_action)
    move_vert(REAR_L_VERT, 0.4, 0)
    move_vert(REAR_R_VERT, 0.4, sleep_action)

    move_knee(FRON_L_KNEE, 0.5, 0)
    move_knee(FRON_R_KNEE, 0.5, sleep_action)
    move_knee(REAR_L_KNEE, 0.5, 0)
    move_knee(REAR_R_KNEE, 0.5, sleep_action)
    move_knee(MIDD_L_KNEE, 0.5, 0)
    move_knee(MIDD_R_KNEE, 0.5, sleep_timing)

def demo_wave(sleep_action, sleep_timing):
    move_vert(FRON_R_VERT, 1, 0)
    move_knee(FRON_R_KNEE, 1, sleep_action)
    try:
        while True:
            move_knee(FRON_R_KNEE, 1, sleep_action)
            move_knee(FRON_R_KNEE, 0, sleep_action)
    except KeyboardInterrupt:
        print("\r:(", file=sys.stderr)
        demo_stand(0, sleep_timing)

def demo_dab(sleep_action, sleep_timing):
    move_vert(MIDD_L_VERT, 0.6, 0)
    move_vert(MIDD_R_VERT, 0.6, sleep_action)
    move_hori(MIDD_L_HORI, 0.7, 0)
    move_hori(MIDD_R_HORI, 0.3, sleep_action)
    move_vert(MIDD_L_VERT, 0.3, 0)
    move_vert(MIDD_R_VERT, 0.3, sleep_action)
    move_vert(FRON_L_VERT, 0.7, 0)
    move_vert(FRON_R_VERT, 0.7, sleep_action)
    move_hori(FRON_L_HORI, 0.4, 0)
    move_hori(FRON_R_HORI, 0.6, sleep_action)
    move_knee(FRON_L_KNEE, 1, 0)
    move_knee(FRON_R_KNEE, 0, sleep_action)
    move_vert(FRON_L_VERT, 0.7, 0)
    move_vert(FRON_R_VERT, 0.3, sleep_action)

    try:
        while True:
            time.sleep(sleep_action)
    except KeyboardInterrupt:
        print("\r:(", file=sys.stderr)
        move_vert(FRON_R_VERT, 1, sleep_timing + 0.5)
        move_vert(FRON_L_VERT, 0.4, 0)
        move_knee(FRON_L_KNEE, 0.5, 0)
        move_knee(FRON_R_KNEE, 0.5, sleep_action)
        move_vert(FRON_R_VERT, 0.5, sleep_timing)
        move_vert(MIDD_L_VERT, 0.6, 0)
        move_vert(MIDD_R_VERT, 0.6, sleep_action + 0.25)
        move_hori(MIDD_L_HORI, 0.5, 0)
        move_hori(MIDD_R_HORI, 0.5, sleep_action)
        move_vert(MIDD_L_VERT, 0.4, 0)
        move_vert(MIDD_R_VERT, 0.4, sleep_timing)

# open_usb(INPUT)

demo_sit(0, 0)

demo_stand(0.25, 1)

wait_interrupt()

demo_wave(0.5, 2)

wait_interrupt()

demo_dab(0.25, 1)

wait_interrupt()

demo_sit(0, 0)
# sys.exit(0)
