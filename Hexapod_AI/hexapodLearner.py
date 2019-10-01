#!/usr/bin/python3
import tensorflow as tf
from hexapod import *
import random

def main():
    hexa = Hexapod(1, 1)
    movement = {0:hexa.move_knee, 1:hexa.move_vert, 2:hexa.move_hori}
    knee_port = [26, 10, 22, 6, 18, 2]
    vert_port = [25, 9, 21, 5, 17, 1]
    hori_port = [24, 8, 20, 4, 16, 0]
    all_port = [knee_port, vert_port, hori_port]
    while True:
        nb_move = random.randint(0, 2)
        nb_leg = random.randint(0, 5)
        nb_deg = random.randint(0, 3000)
        nb_sleep = random.random()
        print(nb_move)
        print(all_port[nb_move][nb_leg], nb_deg, nb_sleep)
        movement[nb_move](all_port[nb_move][nb_leg], nb_deg, nb_sleep)

if __name__== "__main__":
    main()
