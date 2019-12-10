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

    def move_engine(self, engine, angle, speed, sleep_time):
        # print(f"Angle : {angle}"
        angle = convert_angle(angle, engine)
        command = "#%dP%.0fS%d!" % (engine, angle, speed)   # Command to send
        #          #=pin P=position S=speed !=EOL for arduino decode
        self.hexapod_connection.send_command(command, sleep_time)

    def move_knee(self, engine, angle, sleep):
        self.move_engine(engine, angle, self.movements_speed, sleep)

    def move_vert(self, engine, angle, sleep):
        self.move_engine(engine, angle, self.movements_speed, sleep)

    def move_hori(self, engine, angle, sleep):
        self.move_engine(engine, angle, self.movements_speed, sleep)


class HardcodedMovements:
    def __init__(self, connection):
        self.connection = connection
        self.hexapod = Hexapod_movements(connection)
        self.sleep_action_time = 0.25

    def move_kind(self, kind, angle):
        affected_engines = []
        for key in ENGINES:
            if kind in key:
                affected_engines.append(ENGINES[key])
        for engine in affected_engines:
            getattr(self.hexapod, "move_" + kind)(engine, angle, 0)

    def sit(self):
        self.stand()
        self.move_kind("vert", 1)
        time.sleep(0.5)
        self.move_kind("knee", 0)

    def place_hori(self, mode):
        if mode == "para":
            self.move_kind("hori", 0.5)
        elif mode == "normal":
            self.hexapod.move_hori(HORI_FRONT_L, 0.7, 0)
            self.hexapod.move_hori(HORI_FRONT_R, 0.3, 0)
            self.hexapod.move_hori(HORI_MIDDLE_L, 0.5, 0)
            self.hexapod.move_hori(HORI_MIDDLE_R, 0.5, 0)
            self.hexapod.move_hori(HORI_REAR_L, 0.3, 0)
            self.hexapod.move_hori(HORI_REAR_R, 0.7, 0)

    def stand(self):
        self.place_hori('normal')
        self.move_kind("knee", 0.4)
        time.sleep(0.25)
        self.move_kind("vert", 0.6)

    def stand1(self):
        self.move_kind("vert", 0.4)
        self.move_kind("knee", 0.5)
        self.place_hori('normal')

    def stand2(self):
        self.place_hori('normal')
        self.move_kind("vert", 0.2)
        self.move_kind("knee", 0.7)

    def stand3(self):
        self.place_hori('normal')
        self.move_kind("knee", 0.8)
        self.move_kind("vert", 0.1)

    def wave(self):
        self.stand1()
        self.hexapod.move_vert(FRON_R_VERT, 1, 0)
        self.hexapod.move_knee(FRON_R_KNEE, 1, 0.5)
        for i in range(5):
            self.hexapod.move_knee(KNEE_FRONT_R, 1, 0.5)
            self.hexapod.move_knee(KNEE_FRONT_R, 0, 0.5)
        time.sleep(0.5)
        self.stand1()

    def dab(self):
        self.stand1()
        self.hexapod.move_vert(VERT_MIDDLE_L, 0.6, 0)
        self.hexapod.move_vert(VERT_MIDDLE_R, 0.6, self.sleep_action_time)
        self.hexapod.move_hori(HORI_MIDDLE_L, 0.7, 0)
        self.hexapod.move_hori(HORI_MIDDLE_R, 0.3, self.sleep_action_time)
        self.hexapod.move_vert(VERT_MIDDLE_L, 0.3, 0)
        self.hexapod.move_vert(VERT_MIDDLE_R, 0.3, self.sleep_action_time)
        self.hexapod.move_vert(VERT_FRONT_L, 0.7, 0)
        self.hexapod.move_vert(VERT_FRONT_R, 0.7, self.sleep_action_time)
        self.hexapod.move_hori(HORI_FRONT_L, 0.7, 0)
        self.hexapod.move_hori(HORI_FRONT_R, 0.35, self.sleep_action_time)
        self.hexapod.move_knee(KNEE_FRONT_L, 1, 0)
        self.hexapod.move_knee(KNEE_FRONT_R, 0, self.sleep_action_time)
        self.hexapod.move_vert(VERT_FRONT_L, 0.7, 0)
        self.hexapod.move_vert(VERT_FRONT_R, 0.3, self.sleep_action_time)
        time.sleep(2)  # wait for a bit in dab position
        self.stand1()

    def move_knee_up(self):
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
        self.hexapod.move_vert(VERT_FRONT_R, 0.45, 0)
        self.hexapod.move_vert(VERT_MIDDLE_L, 0.45, 0)
        self.hexapod.move_vert(VERT_REAR_R, 0.45, 0.6)

        self.hexapod.move_hori(HORI_FRONT_R, 0.2, 0)
        self.hexapod.move_hori(HORI_MIDDLE_L, 0.7, 0)
        self.hexapod.move_hori(HORI_REAR_R, 0.6, 0.6)

        self.hexapod.move_vert(VERT_FRONT_R, 0.2, 0)
        self.hexapod.move_vert(VERT_MIDDLE_L, 0.2, 0)
        self.hexapod.move_vert(VERT_REAR_R, 0.2, 0.6)

        self.hexapod.move_hori(HORI_MIDDLE_R, 0.5, 0)
        self.hexapod.move_hori(HORI_REAR_L, 0.3, 0)
        self.hexapod.move_hori(HORI_REAR_R, 0.7, 0)

        self.hexapod.move_vert(VERT_FRONT_L, 0.45, 0)
        self.hexapod.move_vert(VERT_MIDDLE_R, 0.45, 0)
        self.hexapod.move_vert(VERT_REAR_L, 0.45, 0.6)

        self.hexapod.move_hori(HORI_FRONT_L, 0.8, 0)
        self.hexapod.move_hori(HORI_MIDDLE_R, 0.4, 0)
        self.hexapod.move_hori(HORI_REAR_L, 0.5, 0.6)

        self.hexapod.move_vert(VERT_FRONT_L, 0.2, 0)
        self.hexapod.move_vert(VERT_MIDDLE_R, 0.2, 0)
        self.hexapod.move_vert(VERT_REAR_L, 0.2, 0.6)

        self.hexapod.move_hori(HORI_FRONT_L, 0.7, 0)
        self.hexapod.move_hori(HORI_FRONT_R, 0.3, 0)
        self.hexapod.move_hori(HORI_MIDDLE_L, 0.5, 0.6)

    def forward_2(self):
        print(self.connection.get_engine_position('all'))

    def stop(self):
        commmand = "XSTOP!"
        self.connection.send_command(commmand, 0)
