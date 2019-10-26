from values import *
import sys
import time

class Hexapod_movements:
    def __init__(self, connection):
        self.hexapod_connection = connection

    def move_engine(self, articulation, deg, speed, tab, sleep_time):
        # We need to know which side the engine is on
        side = articulation <= 15
        # Convert ratio 0-1 to the engine min-max value
        deg = deg * (tab[side][0] - tab[side][1]) + tab[side][1]
        # Command to send to the LynxMotion board
        command = "#%dP%.0fS%d!" % (articulation, deg, speed)
        # #=pin
        # P=position
        # S=speed
        # !=custom EOL for arduino decode
        self.hexapod_connection.send_command(command, sleep_time)

    def move_knee(self, articulation, deg, sleep):
        self.move_engine(articulation, deg, 700, KNEE_VALUES, sleep)

    def move_vert(self, articulation, deg, sleep):
        self.move_engine(articulation, deg, 700, VERT_VALUES, sleep)

    def move_hori(self, articulation, deg, sleep):
        self.move_engine(articulation, deg, 700, HORI_VALUES, sleep)

class HardcodedMovements:
    def __init__(self, connection):
        self.hexapod = Hexapod_movements(connection)
        self.sleep_action_time = 0.25

    def sit(self):
        self.hexapod.move_vert(FRON_L_VERT, 1, 0)
        self.hexapod.move_vert(FRON_R_VERT, 1, self.sleep_action_time)
        self.hexapod.move_vert(REAR_L_VERT, 1, 0)
        self.hexapod.move_vert(REAR_R_VERT, 1, self.sleep_action_time)
        self.hexapod.move_vert(MIDD_L_VERT, 1, 0)
        self.hexapod.move_vert(MIDD_R_VERT, 1, self.sleep_action_time)

        self.hexapod.move_knee(FRON_L_KNEE, 0, 0)
        self.hexapod.move_knee(FRON_R_KNEE, 0, self.sleep_action_time)
        self.hexapod.move_knee(REAR_L_KNEE, 0, 0)
        self.hexapod.move_knee(REAR_R_KNEE, 0, self.sleep_action_time)
        self.hexapod.move_knee(MIDD_L_KNEE, 0, 0)
        self.hexapod.move_knee(MIDD_R_KNEE, 0, 1)

        self.hexapod.move_hori(FRON_L_HORI, 0.5, 0)
        self.hexapod.move_hori(FRON_R_HORI, 0.5, self.sleep_action_time)
        self.hexapod.move_hori(REAR_L_HORI, 0.5, 0)
        self.hexapod.move_hori(REAR_R_HORI, 0.5, self.sleep_action_time)
        self.hexapod.move_hori(MIDD_L_HORI, 0.5, 0)
        self.hexapod.move_hori(MIDD_R_HORI, 0.5, 0)

    def stand(self):
        self.hexapod.move_hori(FRON_L_HORI, 0.5, 0)
        self.hexapod.move_hori(FRON_R_HORI, 0.5, 0)
        self.hexapod.move_hori(REAR_L_HORI, 0.5, 0)
        self.hexapod.move_hori(REAR_R_HORI, 0.5, 0)
        self.hexapod.move_hori(MIDD_L_HORI, 0.5, 0)
        self.hexapod.move_hori(MIDD_R_HORI, 0.5, 0)

        self.hexapod.move_knee(FRON_L_KNEE, 0.3, 0)
        self.hexapod.move_knee(FRON_R_KNEE, 0.3, self.sleep_action_time)
        self.hexapod.move_knee(REAR_L_KNEE, 0.3, 0)
        self.hexapod.move_knee(REAR_R_KNEE, 0.3, self.sleep_action_time)
        self.hexapod.move_knee(MIDD_L_KNEE, 0.3, 0)
        self.hexapod.move_knee(MIDD_R_KNEE, 0.3, self.sleep_action_time)

        self.hexapod.move_vert(MIDD_L_VERT, 0.4, 0)
        self.hexapod.move_vert(MIDD_R_VERT, 0.4, self.sleep_action_time)
        self.hexapod.move_vert(FRON_L_VERT, 0.4, 0)
        self.hexapod.move_vert(FRON_R_VERT, 0.4, self.sleep_action_time)
        self.hexapod.move_vert(REAR_L_VERT, 0.4, 0)
        self.hexapod.move_vert(REAR_R_VERT, 0.4, self.sleep_action_time)

        self.hexapod.move_knee(FRON_L_KNEE, 0.5, 0)
        self.hexapod.move_knee(FRON_R_KNEE, 0.5, self.sleep_action_time)
        self.hexapod.move_knee(REAR_L_KNEE, 0.5, 0)
        self.hexapod.move_knee(REAR_R_KNEE, 0.5, self.sleep_action_time)
        self.hexapod.move_knee(MIDD_L_KNEE, 0.5, 0)
        self.hexapod.move_knee(MIDD_R_KNEE, 0.5, 0)

    def wave(self):
        self.hexapod.move_vert(FRON_R_VERT, 1, 0)
        self.hexapod.move_knee(FRON_R_KNEE, 1, 0.5)

        for i in range(5):
            self.hexapod.move_knee(FRON_R_KNEE, 1, 0.5)
            self.hexapod.move_knee(FRON_R_KNEE, 0, 0.5)
        time.sleep(0.5)
        self.stand()

    def dab(self):
        self.hexapod.move_vert(MIDD_L_VERT, 0.6, 0)
        self.hexapod.move_vert(MIDD_R_VERT, 0.6, self.sleep_action_time)
        self.hexapod.move_hori(MIDD_L_HORI, 0.7, 0)
        self.hexapod.move_hori(MIDD_R_HORI, 0.3, self.sleep_action_time)
        self.hexapod.move_vert(MIDD_L_VERT, 0.3, 0)
        self.hexapod.move_vert(MIDD_R_VERT, 0.3, self.sleep_action_time)
        self.hexapod.move_vert(FRON_L_VERT, 0.7, 0)
        self.hexapod.move_vert(FRON_R_VERT, 0.7, self.sleep_action_time)
        self.hexapod.move_hori(FRON_L_HORI, 0.4, 0)
        self.hexapod.move_hori(FRON_R_HORI, 0.6, self.sleep_action_time)
        self.hexapod.move_knee(FRON_L_KNEE, 1, 0)
        self.hexapod.move_knee(FRON_R_KNEE, 0, self.sleep_action_time)
        self.hexapod.move_vert(FRON_L_VERT, 0.7, 0)
        self.hexapod.move_vert(FRON_R_VERT, 0.3, self.sleep_action_time)

        time.sleep(2) # wait for a bit in dab position
        # WTF why don't we call stand here ??

        self.hexapod.move_vert(FRON_R_VERT, 1, self.sleep_action_time)
        self.hexapod.move_vert(FRON_L_VERT, 0.4, 0)
        self.hexapod.move_knee(FRON_L_KNEE, 0.5, 0)
        self.hexapod.move_knee(FRON_R_KNEE, 0.5, self.sleep_action_time)
        self.hexapod.move_vert(FRON_R_VERT, 0.5, self.sleep_action_time)
        self.hexapod.move_vert(MIDD_L_VERT, 0.6, 0)
        self.hexapod.move_vert(MIDD_R_VERT, 0.6, self.sleep_action_time + 0.25)
        self.hexapod.move_hori(MIDD_L_HORI, 0.5, 0)
        self.hexapod.move_hori(MIDD_R_HORI, 0.5, self.sleep_action_time)
        self.hexapod.move_vert(MIDD_L_VERT, 0.4, 0)
        self.hexapod.move_vert(MIDD_R_VERT, 0.4, self.sleep_action_time)

    def forward(self):
        # on leve 3 pattes
        self.hexapod.move_knee(FRON_R_VERT, 0.35, 0)
        self.hexapod.move_knee(MIDD_L_VERT, 0.35, 0)
        self.hexapod.move_knee(REAR_R_VERT, 0.35, 1)

        # on avance les 3 autres
        self.hexapod.move_hori(FRON_L_HORI, 0.35, 0)
        self.hexapod.move_hori(MIDD_R_HORI, 0.65, 0)
        self.hexapod.move_hori(REAR_L_HORI, 0.35, 1)

        # on avance les 3 en l'air
        self.hexapod.move_hori(FRON_R_HORI, 0.35, 0)
        self.hexapod.move_hori(MIDD_L_HORI, 0.65, 0)
        self.hexapod.move_hori(REAR_R_HORI, 0.35, 1)

        # on repose les 3 pattes
        self.hexapod.move_knee(FRON_R_VERT, 0.5, 0)
        self.hexapod.move_knee(MIDD_L_VERT, 0.5, 0)
        self.hexapod.move_knee(REAR_R_VERT, 0.5, 1)

        # ----------------------------------

        self.hexapod.move_knee(FRON_L_VERT, 0.35, 0)
        self.hexapod.move_knee(MIDD_R_VERT, 0.35, 0)
        self.hexapod.move_knee(REAR_L_VERT, 0.35, 1)

        # on avance les 3 autres
        self.hexapod.move_hori(FRON_L_HORI, 0.65, 0)
        self.hexapod.move_hori(MIDD_R_HORI, 0.35, 0)
        self.hexapod.move_hori(REAR_L_HORI, 0.65, 1)

        # on avance les 3 en l'air
        self.hexapod.move_hori(FRON_R_HORI, 0.65, 0)
        self.hexapod.move_hori(MIDD_L_HORI, 0.35, 0)
        self.hexapod.move_hori(REAR_R_HORI, 0.65, 1)

        # on repose les 3 pattes
        self.hexapod.move_knee(FRON_L_VERT, 0.5, 0)
        self.hexapod.move_knee(MIDD_R_VERT, 0.5, 0)
        self.hexapod.move_knee(REAR_L_VERT, 0.5, 1)
