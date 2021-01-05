from values import *
import sys
import time
import threading
import random

ENGINES = {
    "fron_l_hori": HORI_FRONT_L,
    "fron_l_knee": KNEE_FRONT_L,
    "fron_l_vert": VERT_FRONT_L,
    "fron_r_hori": HORI_FRONT_R,
    "fron_r_knee": KNEE_FRONT_R,
    "fron_r_vert": VERT_FRONT_R,
    "midd_l_hori": HORI_MIDDLE_L,
    "midd_l_knee": KNEE_MIDDLE_L,
    "midd_l_vert": VERT_MIDDLE_L,
    "midd_r_hori": HORI_MIDDLE_R,
    "midd_r_knee": KNEE_MIDDLE_R,
    "midd_r_vert": VERT_MIDDLE_R,
    "rear_l_hori": HORI_REAR_L,
    "rear_l_knee": KNEE_REAR_L,
    "rear_l_vert": VERT_REAR_L,
    "rear_r_hori": HORI_REAR_R,
    "rear_r_knee": KNEE_REAR_R,
    "rear_r_vert": VERT_REAR_R
}


class Hexapod_movements:
    def __init__(self, connection):
        self.hexapod_connection = connection
        self.movements_speed = 700
        self.string_to_send = ""

    def send_command_group(self):
        self.string_to_send += "!"
        self.hexapod_connection.send_command(self.string_to_send)
        self.string_to_send = ""

    def add_command_to_command_group(self, engine, angle, speed):
        angle = convert_angle(angle, engine)
        command = "#%dP%.0fS%d" % (engine, angle, speed)
        self.string_to_send += command

    def send_command(self, engine, angle, speed):
        angle = convert_angle(angle, engine)
        command = "#%dP%.0fS%d" % (engine, angle, speed)
        #=pin P=position S=speed !=EOL for arduino decode
        self.hexapod_connection.send_command(command)

    def move(self, engine, angle, sleep=0, directly_send=False, send=False, sleep_time=False):
        if directly_send == False:
            self.add_command_to_command_group(engine, angle, self.movements_speed)
        else:
            self.send_command(engine, angle, self.movements_speed)
        if send == True:
            self.send_command_group()
        if sleep_time != None:
            time.sleep(sleep_time)

    def set_movements_speed(self, new_speed):
        if new_speed == -1:
            self.movements_speed = 700
        else:
            self.movements_speed = new_speed

class HardcodedMovements:
    def __init__(self, connection):
        self.connection = connection
        self.hexapod = Hexapod_movements(connection)
        self.sleep_action_time = 0.25

    def set_actions_speed(self, new_speed):
        self.hexapod.set_movements_speed(new_speed)

    def move_kind(self, kind, angle, send=None):
        affected_engines = []
        for key in ENGINES:
            if kind in key:
                affected_engines.append(ENGINES[key])
        for engine in affected_engines:
            self.hexapod.move(engine, angle)
        if send != None:
            self.hexapod.send_command_group()

    def sit(self):
        self.stand()
        self.move_kind("vert", 1, send=True)
        time.sleep(0.5)
        self.move_kind("knee", 0, send=True)

    def place_hori(self, mode):
        if mode == "para":
            self.move_kind("hori", 0.5)
        elif mode == "normal":
            self.hexapod.move(HORI_FRONT_L, 0.7)
            self.hexapod.move(HORI_FRONT_R, 0.3)
            self.hexapod.move(HORI_MIDDLE_L, 0.5)
            self.hexapod.move(HORI_MIDDLE_R, 0.5)
            self.hexapod.move(HORI_REAR_L, 0.3)
            self.hexapod.move(HORI_REAR_R, 0.7, send=True)

    def stand(self):
        self.place_hori('normal')
        self.move_kind("knee", 0.4, send=True)
        time.sleep(0.25)
        self.move_kind("vert", 0.6, send=True)

    def stand1(self):
        self.place_hori('normal')
        self.move_kind("knee", 0.4, send=True)
        time.sleep(0.25)
        self.move_kind("vert", 0.5, send=True)

    def stand2(self):
        self.place_hori('normal')
        self.move_kind("knee", 0.7, send=True)
        time.sleep(0.25)
        self.move_kind("vert", 0.3, send=True)

    def stand3(self):
        self.place_hori('normal')
        self.move_kind("vert", 0.1, send=True)
        self.move_kind("knee", 0.8, send=True)

    def wave(self):
        self.stand1()
        self.hexapod.move(VERT_FRONT_R, 0.7, directly_send=True)
        for _ in range(5):
            self.hexapod.move(KNEE_FRONT_R, 1, directly_send=True)
            time.sleep(0.5)
            self.hexapod.move(KNEE_FRONT_R, 0, directly_send=True)
            time.sleep(0.5)
        self.stand1()

    def dab(self):
        self.stand1()
        time.sleep(3)
        self.hexapod.move(VERT_MIDDLE_L, 0.6, 0)
        self.hexapod.move(VERT_MIDDLE_R, 0.6, self.sleep_action_time, send=True)

        self.hexapod.move(HORI_MIDDLE_L, 0.7, 0)
        self.hexapod.move(HORI_MIDDLE_R, 0.3, self.sleep_action_time, send=True)

        self.hexapod.move(VERT_MIDDLE_L, 0.3, 0)
        self.hexapod.move(VERT_MIDDLE_R, 0.3, self.sleep_action_time, send=True)

        self.hexapod.move(VERT_FRONT_L, 0.7, 0)
        self.hexapod.move(VERT_FRONT_R, 0.7, self.sleep_action_time)
        self.hexapod.move(HORI_FRONT_L, 0.7, 0)
        self.hexapod.move(HORI_FRONT_R, 0.35, self.sleep_action_time)
        self.hexapod.move(KNEE_FRONT_L, 1, 0)
        self.hexapod.move(KNEE_FRONT_R, 0, self.sleep_action_time)
        self.hexapod.move(VERT_FRONT_L, 0.7, 0)
        self.hexapod.move(VERT_FRONT_R, 0.3, self.sleep_action_time, send=True)
        time.sleep(2)  # wait for a bit in dab position
        self.stand1()

    def move_up(self):
        kind = 'vert'
        affected_engines = []
        for key in ENGINES:
            if kind in key:
                affected_engines.append(ENGINES[key])
        for engine in affected_engines:
            getattr(self.hexapod, "move_" + kind)(engine, 0.6, 0)
            time.sleep(0.5)
            getattr(self.hexapod, "move_" + kind)(engine, 0.2, 0)

    def rotate_right(self):
        self.continue_movement = True
        self.thread_walk = threading.Thread(target=self.rotate, args=('r'))
        self.thread_walk.daemon = True
        self.thread_walk.start()

    def rotate_left(self):
        self.continue_movement = True
        self.thread_walk = threading.Thread(target=self.rotate, args=('l'))
        self.thread_walk.daemon = True
        self.thread_walk.start()

    def rotate(self, direction):
        self.hexapod.set_movements_speed(1500)
        side = 1 if direction == 'r' else -1

        # LEVE LES PATES
        self.hexapod.move(VERT_FRONT_R, 0.6)
        self.hexapod.move(VERT_MIDDLE_L, 0.6)
        self.hexapod.move(VERT_REAR_R, 0.6, send=True)
        time.sleep(0.2)

        # BOUGE VERS L"AVANT
        self.hexapod.move(HORI_FRONT_R, 0.3 + (0.2 * side))
        self.hexapod.move(HORI_MIDDLE_L, 0.5 + (0.2 * side))
        self.hexapod.move(HORI_REAR_R, 0.7 + (0.2 * side))

        # On tourne les pates au sol
        self.hexapod.move(HORI_FRONT_L, 0.7 - (0.1 * side))
        self.hexapod.move(HORI_MIDDLE_R, 0.5 - (0.1 * side))
        self.hexapod.move(HORI_REAR_L, 0.3 - (0.1 * side), send=True)
        time.sleep(0.2)

        # on pose les pates qui etaient en l'air
        self.hexapod.move(VERT_FRONT_R, 0.5)
        self.hexapod.move(VERT_MIDDLE_L, 0.5)
        self.hexapod.move(VERT_REAR_R, 0.5, send=True)
        time.sleep(0.2)

        # On leve le 2e set de pates
        self.hexapod.move(VERT_FRONT_L, 0.7)
        self.hexapod.move(VERT_MIDDLE_R, 0.7)
        self.hexapod.move(VERT_REAR_L, 0.7, send=True)
        time.sleep(0.2)


        # on avance celles au sol
        self.hexapod.move(HORI_FRONT_R, 0.3 - (0.2 * side))
        self.hexapod.move(HORI_MIDDLE_L, 0.5 - (0.2 * side))
        self.hexapod.move(HORI_REAR_R, 0.7 - (0.2 * side))


        # on les avance
        self.hexapod.move(HORI_FRONT_L, 0.7 - (0.2 * side))
        self.hexapod.move(HORI_MIDDLE_R, 0.5 - (0.2 * side))
        self.hexapod.move(HORI_REAR_L, 0.3 - (0.2 * side), send=True)
        time.sleep(0.2)

        # On les poses
        self.hexapod.move(VERT_FRONT_L, 0.5)
        self.hexapod.move(VERT_MIDDLE_R, 0.5)
        self.hexapod.move(VERT_REAR_L, 0.5, send=True)
        time.sleep(0.1)
        self.hexapod.set_movements_speed(-1)

        if self.continue_movement == False:
            exit(0)
        self.rotate(direction)

    def walk_forward(self):
        self.hexapod.set_movements_speed(1500)
        # LEVE LES PATES
        self.hexapod.move(VERT_FRONT_R, 0.6)
        self.hexapod.move(VERT_MIDDLE_L, 0.6)
        self.hexapod.move(VERT_REAR_R, 0.6, send=True)
        time.sleep(0.2)

        # BOUGE VERS L"AVANT
        self.hexapod.move(HORI_FRONT_R, 0.2)
        self.hexapod.move(HORI_MIDDLE_L, 0.6)
        self.hexapod.move(HORI_REAR_R, 0.6)


        # On Avance les pates au sol
        self.hexapod.move(HORI_FRONT_L, 0.5)
        self.hexapod.move(HORI_MIDDLE_R, 0.6)
        self.hexapod.move(HORI_REAR_L, 0.2, send=True)
        time.sleep(0.2)

        # on pose les pates qui etaient en l'air
        self.hexapod.move(VERT_FRONT_R, 0.5)
        self.hexapod.move(VERT_MIDDLE_L, 0.5)
        self.hexapod.move(VERT_REAR_R, 0.5, send=True)
        time.sleep(0.2)

        # On leve le 2e set de pates
        self.hexapod.move(VERT_FRONT_L, 0.7)
        self.hexapod.move(VERT_MIDDLE_R, 0.7)
        self.hexapod.move(VERT_REAR_L, 0.7, send=True)
        time.sleep(0.2)

        # on avance celles au sol
        self.hexapod.move(HORI_FRONT_R, 0.4)
        self.hexapod.move(HORI_MIDDLE_L, 0.4)
        self.hexapod.move(HORI_REAR_R, 0.8)

        # on les avance
        self.hexapod.move(HORI_FRONT_L, 0.8)
        self.hexapod.move(HORI_MIDDLE_R, 0.4)
        self.hexapod.move(HORI_REAR_L, 0.4, send=True)
        time.sleep(0.2)

        # On les poses
        self.hexapod.move(VERT_FRONT_L, 0.5)
        self.hexapod.move(VERT_MIDDLE_R, 0.5)
        self.hexapod.move(VERT_REAR_L, 0.5, send=True)
        time.sleep(0.1)
        self.hexapod.set_movements_speed(-1)
        if self.continue_movement == False:
            exit(0)
        self.walk_forward()

    def walk_backward(self):
        self.hexapod.set_movements_speed(1500)

        # LEVE LES PATES
        self.hexapod.move(VERT_FRONT_R, 0.6)
        self.hexapod.move(VERT_MIDDLE_L, 0.6)
        self.hexapod.move(VERT_REAR_R, 0.6, send=True)
        time.sleep(0.2)

        # BOUGE VERS L"AVANT
        self.hexapod.move(HORI_FRONT_R, 0.5)
        self.hexapod.move(HORI_MIDDLE_L, 0.4)
        self.hexapod.move(HORI_REAR_R, 0.8)

        # On Avance les pates au sol
        self.hexapod.move(HORI_FRONT_L, 0.8)
        self.hexapod.move(HORI_MIDDLE_R, 0.4)
        self.hexapod.move(HORI_REAR_L, 0.4, send=True)
        time.sleep(0.2)

        # on pose les pates qui etaient en l'air
        self.hexapod.move(VERT_FRONT_R, 0.5)
        self.hexapod.move(VERT_MIDDLE_L, 0.5)
        self.hexapod.move(VERT_REAR_R, 0.5, send=True)
        time.sleep(0.2)
        # On leve le 2e set de pates
        self.hexapod.move(VERT_FRONT_L, 0.7)
        self.hexapod.move(VERT_MIDDLE_R, 0.7)
        self.hexapod.move(VERT_REAR_L, 0.7, send=True)
        time.sleep(0.2)

        # on avance celles au sol
        self.hexapod.move(HORI_FRONT_R, 0.2)
        self.hexapod.move(HORI_MIDDLE_L, 0.6)
        self.hexapod.move(HORI_REAR_R, 0.6)

        # on les avance
        self.hexapod.move(HORI_FRONT_L, 0.6)
        self.hexapod.move(HORI_MIDDLE_R, 0.6)
        self.hexapod.move(HORI_REAR_L, 0.2, send=True)
        time.sleep(0.2)

        # On les poses
        self.hexapod.move(VERT_FRONT_L, 0.5)
        self.hexapod.move(VERT_MIDDLE_R, 0.5)
        self.hexapod.move(VERT_REAR_L, 0.5, send=True)
        time.sleep(0.1)
        self.hexapod.set_movements_speed(-1)
        if self.continue_movement == False:
            exit(0)
        self.walk_backward()

    def forward(self):
        self.continue_movement = True
        self.thread_walk = threading.Thread(target=self.walk_forward, args=())
        self.thread_walk.daemon = True
        self.thread_walk.start()

    def backward(self):
        self.continue_movement = True
        self.thread_walk = threading.Thread(target=self.walk_backward, args=())
        self.thread_walk.daemon = True
        self.thread_walk.start()

    def stop(self):
        self.continue_movement = False
        self.thread_walk.join()

    def replace_legs(self):
        vert_engines = [VERT_FRONT_L, VERT_MIDDLE_L, VERT_REAR_L, VERT_FRONT_R, VERT_MIDDLE_R, VERT_REAR_R]
        random.shuffle(vert_engines)

        self.hexapod.set_movements_speed(2300)
        for eng in vert_engines:
            self.hexapod.move(eng, 0.7, send=True, sleep_time=0.1)
            self.hexapod.move(eng, 0.5, send=True)
        self.hexapod.set_movements_speed(-1)