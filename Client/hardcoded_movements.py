from values import *
import sys
import time

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
        print(command)
        self.string_to_send += command

    def send_command(self, engine, angle, speed):
        angle = convert_angle(angle, engine)
        command = "#%dP%.0fS%d" % (engine, angle, speed)   # Command to send
        self.string_to_send += command
        #          #=pin P=position S=speed !=EOL for arduino decode
        self.hexapod_connection.send_command(command)

    def move(self, engine, angle, sleep=0, directly_send=False):
        if directly_send == False:
            self.add_command_to_command_group(engine, angle, self.movements_speed)
        else:
            self.send_command(engine, angle, self.movements_speed)

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

    def move_kind(self, kind, angle):
        affected_engines = []
        for key in ENGINES:
            if kind in key:
                affected_engines.append(ENGINES[key])
        for engine in affected_engines:
            self.hexapod.move(engine, angle)

    def sit(self): # OK
        self.stand()
        self.move_kind("vert", 1)
        self.hexapod.send_command_group()
        time.sleep(0.5)
        self.move_kind("knee", 0)
        self.hexapod.send_command_group()

    def place_hori(self, mode):
        if mode == "para":
            self.move_kind("hori", 0.5)
        elif mode == "normal":
            self.hexapod.move(HORI_FRONT_L, 0.7)
            self.hexapod.move(HORI_FRONT_R, 0.3)
            self.hexapod.move(HORI_MIDDLE_L, 0.5)
            self.hexapod.move(HORI_MIDDLE_R, 0.5)
            self.hexapod.move(HORI_REAR_L, 0.3)
            self.hexapod.move(HORI_REAR_R, 0.7)
            self.hexapod.send_command_group()

    def stand(self): # OK
        self.place_hori('normal')
        self.move_kind("knee", 0.4)
        self.hexapod.send_command_group()
        time.sleep(0.25)
        self.move_kind("vert", 0.6)
        self.hexapod.send_command_group()

    def stand1(self):
        self.move_kind("vert", 0.4)
        self.hexapod.send_command_group()
        self.move_kind("knee", 0.6)
        self.hexapod.send_command_group()
        self.place_hori('normal')

    def stand2(self):
        self.place_hori('normal')
        self.move_kind("vert", 0.3)
        self.hexapod.send_command_group()
        self.move_kind("knee", 0.7)
        self.hexapod.send_command_group()

    def stand3(self):
        self.place_hori('normal')
        self.move_kind("vert", 0.1)
        self.hexapod.send_command_group()
        self.move_kind("knee", 0.8)
        self.hexapod.send_command_group()

    def wave(self):
        self.stand1()
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
        self.hexapod.move(VERT_MIDDLE_R, 0.6, self.sleep_action_time)

        self.hexapod.send_command_group()
        self.hexapod.move(HORI_MIDDLE_L, 0.7, 0)
        self.hexapod.move(HORI_MIDDLE_R, 0.3, self.sleep_action_time)

        self.hexapod.send_command_group()
        self.hexapod.move(VERT_MIDDLE_L, 0.3, 0)
        self.hexapod.move(VERT_MIDDLE_R, 0.3, self.sleep_action_time)

        self.hexapod.send_command_group()
        self.hexapod.move(VERT_FRONT_L, 0.7, 0)
        self.hexapod.move(VERT_FRONT_R, 0.7, self.sleep_action_time)
        self.hexapod.move(HORI_FRONT_L, 0.7, 0)
        self.hexapod.move(HORI_FRONT_R, 0.35, self.sleep_action_time)
        self.hexapod.move(KNEE_FRONT_L, 1, 0)
        self.hexapod.move(KNEE_FRONT_R, 0, self.sleep_action_time)
        self.hexapod.move(VERT_FRONT_L, 0.7, 0)
        self.hexapod.move(VERT_FRONT_R, 0.3, self.sleep_action_time)
        self.hexapod.send_command_group()
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

    def forward(self):
        #  command = "RH 2100 RM 1400 RL 1000 LH 500 LM 1400 LL 1800 VS 500 LF 800 LR 1700 RF 1700 RR 800 HT 500 XL 20 XR 20 XS 170!"
        #  self.connection.send_command(command, 0)
        self.hexapod.move(VERT_FRONT_R, 0.45, 0)
        self.hexapod.move(VERT_MIDDLE_L, 0.45, 0)
        self.hexapod.move(VERT_REAR_R, 0.45, 0.6)

        self.hexapod.move(HORI_FRONT_R, 0.2, 0)
        self.hexapod.move(HORI_MIDDLE_L, 0.7, 0)
        self.hexapod.move(HORI_REAR_R, 0.6, 0.6)

        self.hexapod.move(VERT_FRONT_R, 0.2, 0)
        self.hexapod.move(VERT_MIDDLE_L, 0.2, 0)
        self.hexapod.move(VERT_REAR_R, 0.2, 0.6)

        self.hexapod.move(HORI_MIDDLE_R, 0.5, 0)
        self.hexapod.move(HORI_REAR_L, 0.3, 0)
        self.hexapod.move(HORI_REAR_R, 0.7, 0)

        self.hexapod.move(VERT_FRONT_L, 0.45, 0)
        self.hexapod.move(VERT_MIDDLE_R, 0.45, 0)
        self.hexapod.move(VERT_REAR_L, 0.45, 0.6)

        self.hexapod.move(HORI_FRONT_L, 0.8, 0)
        self.hexapod.move(HORI_MIDDLE_R, 0.4, 0)
        self.hexapod.move(HORI_REAR_L, 0.5, 0.6)

        self.hexapod.move(VERT_FRONT_L, 0.2, 0)
        self.hexapod.move(VERT_MIDDLE_R, 0.2, 0)
        self.hexapod.move(VERT_REAR_L, 0.2, 0.6)

        self.hexapod.move(HORI_FRONT_L, 0.7, 0)
        self.hexapod.move(HORI_FRONT_R, 0.3, 0)
        self.hexapod.move(HORI_MIDDLE_L, 0.5, 0.6)

    def forward_2(self):
        print(self.connection.get_engine_position('all'))

    def stop(self):
        commmand = "XSTOP!"
        self.connection.send_command(commmand, 0)
