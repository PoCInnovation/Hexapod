#!/usr/bin/python3
import tensorflow as tf
import engine_mouvements as move
import random

def main():
    movement = {0:move.move_knee, 1:move.move_vert, 2:move.move_hori}
    knee_port = [26, 10, 22, 6, 18, 2]
    vert_port = [25, 9, 21, 5, 17, 1]
    hori_port = [24, 8, 20, 4, 16, 0]
    all_port = [knee_port, vert_port, hori_port]
    while True:
        nb_move = random.randint(0, 2)
        nb_leg = random.randint(0, 5)
        nb_deg = random.randint(0, 3000)
        nb_sleep = random.random()
        print (nb_move)
        print (all_port[nb_move][nb_leg], nb_deg, nb_sleep)
        movement[nb_move](all_port[nb_move][nb_leg], nb_deg, nb_sleep)

if __name__== "__main__":
    main()