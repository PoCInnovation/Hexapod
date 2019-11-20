from values import *
import sys
import time

ENGINES = {
    "rear_r_hori": REAR_R_HORI,
    "rear_r_vert": REAR_R_VERT,
    "rear_r_knee": REAR_R_KNEE,
    "rear_l_hori": REAR_L_HORI,
    "rear_l_vert": REAR_L_VERT,
    "rear_l_knee": REAR_L_KNEE,
    "midd_r_hori": MIDDLE_R_HORI,
    "midd_r_vert": MIDDLE_R_VERT,
    "midd_r_knee": MIDDLE_R_KNEE,
    "midd_l_hori": MIDDLE_L_HORI,
    "midd_l_vert": MIDDLE_L_VERT,
    "midd_l_knee": MIDDLE_L_KNEE,
    "fron_r_hori": FRONT_R_HORI,
    "fron_r_vert": FRONT_R_VERT,
    "fron_r_knee": FRONT_R_KNEE,
    "fron_l_hori": FRONT_L_HORI,
    "fron_l_vert": FRONT_L_VERT,
    "fron_l_knee": FRONT_L_KNEE
}


class Hexapod_movements:
    def __init__(self, connection):
        self.hexapod_connection = connection
        self.movements_speed = 700

    def move_engine(self, engine, angle, speed, sleep_time):
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
            getattr(self.hexapod, "move_" + kind)(engine, deg, 0)

    def sit(self):
        self.stand()
        self.move_kind("vert", 1)
        time.sleep(0.5)
        self.move_kind("knee", 0)

    def place_hori(self, mode):
        if mode == "para":
            self.move_kind("hori", 0.5)
        elif mode == "normal":
            self.hexapod.move_hori(FRONT_L_HORI, 0.7, 0)
            self.hexapod.move_hori(FRONT_R_HORI, 0.3, 0)
            self.hexapod.move_hori(MIDDLE_L_HORI, 0.5, 0)
            self.hexapod.move_hori(MIDDLE_R_HORI, 0.5, 0)
            self.hexapod.move_hori(REAR_L_HORI, 0.3, 0)
            self.hexapod.move_hori(REAR_R_HORI, 0.7, 0)

    def stand(self):
        self.place_hori('normal')
        self.move_kind("knee", 0.4)
        time.sleep(0.25)
        self.move_kind("vert", 0.6)

    def stand1(self):
        self.place_hori('normal')
        self.move_kind("vert", 0.4)
        self.move_kind("knee", 0.5)

    def stand2(self):
        self.place_hori('normal')
        self.move_kind("vert", 0.2)
        self.move_kind("knee", 0.7)

    def stand3(self):
        self.place_hori('normal')
        self.move_kind("knee", 0.8)
        self.move_kind("vert", 0.1)

    def wave(self):
        self.hexapod.move_vert(FRONT_R_VERT, 1, 0)
        self.hexapod.move_knee(FRONT_R_KNEE, 1, 0.5)
        self.stand1()
        for i in range(5):
            self.hexapod.move_knee(FRONT_R_KNEE, 1, 0.5)
            self.hexapod.move_knee(FRONT_R_KNEE, 0, 0.5)
        time.sleep(0.5)
        self.stand1()

    def dab(self):
        self.hexapod.move_vert(MIDDLE_L_VERT, 0.6, 0)
        self.hexapod.move_vert(MIDDLE_R_VERT, 0.6, self.sleep_action_time)
        self.hexapod.move_hori(MIDDLE_L_HORI, 0.7, 0)
        self.hexapod.move_hori(MIDDLE_R_HORI, 0.3, self.sleep_action_time)
        self.hexapod.move_vert(MIDDLE_L_VERT, 0.3, 0)
        self.hexapod.move_vert(MIDDLE_R_VERT, 0.3, self.sleep_action_time)
        self.hexapod.move_vert(FRONT_L_VERT, 0.7, 0)
        self.hexapod.move_vert(FRONT_R_VERT, 0.7, self.sleep_action_time)
        self.hexapod.move_hori(FRONT_L_HORI, 0.4, 0)
        self.hexapod.move_hori(FRONT_R_HORI, 0.6, self.sleep_action_time)
        self.hexapod.move_knee(FRONT_L_KNEE, 1, 0)
        self.hexapod.move_knee(FRONT_R_KNEE, 0, self.sleep_action_time)
        self.hexapod.move_vert(FRONT_L_VERT, 0.7, 0)
        self.hexapod.move_vert(FRONT_R_VERT, 0.3, self.sleep_action_time)

        time.sleep(2)  # wait for a bit in dab position
        # self.stand() # <-- TO BE TESTED

        self.hexapod.move_vert(FRONT_R_VERT, 1, self.sleep_action_time)
        self.hexapod.move_vert(FRONT_L_VERT, 0.4, 0)
        self.hexapod.move_knee(FRONT_L_KNEE, 0.5, 0)
        self.hexapod.move_knee(FRONT_R_KNEE, 0.5, self.sleep_action_time)
        self.hexapod.move_vert(FRONT_R_VERT, 0.5, self.sleep_action_time)
        self.hexapod.move_vert(MIDDLE_L_VERT, 0.6, 0)
        self.hexapod.move_vert(MIDDLE_R_VERT, 0.6, self.sleep_action_time + 0.25)
        self.hexapod.move_hori(MIDDLE_L_HORI, 0.5, 0)
        self.hexapod.move_hori(MIDDLE_R_HORI, 0.5, self.sleep_action_time)
        self.hexapod.move_vert(MIDDLE_L_VERT, 0.4, 0)
        self.hexapod.move_vert(MIDDLE_R_VERT, 0.4, self.sleep_action_time)

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
        self.hexapod.move_vert(FRONT_R_VERT, 0.45, 0)
        self.hexapod.move_vert(MIDDLE_L_VERT, 0.45, 0)
        self.hexapod.move_vert(REAR_R_VERT, 0.45, 0.6)

        self.hexapod.move_hori(FRONT_R_HORI, 0.2, 0)
        self.hexapod.move_hori(MIDDLE_L_HORI, 0.7, 0)
        self.hexapod.move_hori(REAR_R_HORI, 0.6, 0.6)

        self.hexapod.move_vert(FRONT_R_VERT, 0.2, 0)
        self.hexapod.move_vert(MIDDLE_L_VERT, 0.2, 0)
        self.hexapod.move_vert(REAR_R_VERT, 0.2, 0.6)

        self.hexapod.move_hori(MIDDLE_R_HORI, 0.5, 0)
        self.hexapod.move_hori(REAR_L_HORI, 0.3, 0)
        self.hexapod.move_hori(REAR_R_HORI, 0.7, 0)

        self.hexapod.move_vert(FRONT_L_VERT, 0.45, 0)
        self.hexapod.move_vert(MIDDLE_R_VERT, 0.45, 0)
        self.hexapod.move_vert(REAR_L_VERT, 0.45, 0.6)

        self.hexapod.move_hori(FRONT_L_HORI, 0.8, 0)
        self.hexapod.move_hori(MIDDLE_R_HORI, 0.4, 0)
        self.hexapod.move_hori(REAR_L_HORI, 0.5, 0.6)

        self.hexapod.move_vert(FRONT_L_VERT, 0.2, 0)
        self.hexapod.move_vert(MIDDLE_R_VERT, 0.2, 0)
        self.hexapod.move_vert(REAR_L_VERT, 0.2, 0.6)

        self.hexapod.move_hori(FRONT_L_HORI, 0.7, 0)
        self.hexapod.move_hori(FRONT_R_HORI, 0.3, 0)
        self.hexapod.move_hori(MIDDLE_L_HORI, 0.5, 0.6)

    def forward_2(self):
        print(self.connection.get_engine_position('all'))

    def stop(self):
        commmand = "XSTOP!"
        self.connection.send_command(commmand, 0)
