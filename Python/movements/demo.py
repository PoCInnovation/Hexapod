from values import *


class HexapodDemo:
    def __init__(self, hexapod):
        self.hexapod = hexapod

    def demo_sit(self, sleep_action, sleep_timing):
        self.hexapod.move_vert(FRON_L_VERT, 1, 0)
        self.hexapod.move_vert(FRON_R_VERT, 1, sleep_action)
        self.hexapod.move_vert(REAR_L_VERT, 1, 0)
        self.hexapod.move_vert(REAR_R_VERT, 1, sleep_action)
        self.hexapod.move_vert(MIDD_L_VERT, 1, 0)
        self.hexapod.move_vert(MIDD_R_VERT, 1, sleep_action)

        self.hexapod.move_knee(FRON_L_KNEE, 0, 0)
        self.hexapod.move_knee(FRON_R_KNEE, 0, sleep_action)
        self.hexapod.move_knee(REAR_L_KNEE, 0, 0)
        self.hexapod.move_knee(REAR_R_KNEE, 0, sleep_action)
        self.hexapod.move_knee(MIDD_L_KNEE, 0, 0)
        self.hexapod.move_knee(MIDD_R_KNEE, 0, 1)

        self.hexapod.move_hori(FRON_L_HORI, 0.5, 0)
        self.hexapod.move_hori(FRON_R_HORI, 0.5, sleep_action)
        self.hexapod.move_hori(REAR_L_HORI, 0.5, 0)
        self.hexapod.move_hori(REAR_R_HORI, 0.5, sleep_action)
        self.hexapod.move_hori(MIDD_L_HORI, 0.5, 0)
        self.hexapod.move_hori(MIDD_R_HORI, 0.5, sleep_timing)

    def demo_stand(self, sleep_action, sleep_timing):
        self.hexapod.move_hori(FRON_L_HORI, 0.5, 0)
        self.hexapod.move_hori(FRON_R_HORI, 0.5, 0)
        self.hexapod.move_hori(REAR_L_HORI, 0.5, 0)
        self.hexapod.move_hori(REAR_R_HORI, 0.5, 0)
        self.hexapod.move_hori(MIDD_L_HORI, 0.5, 0)
        self.hexapod.move_hori(MIDD_R_HORI, 0.5, 0)

        self.hexapod.move_knee(FRON_L_KNEE, 0.3, 0)
        self.hexapod.move_knee(FRON_R_KNEE, 0.3, sleep_action)
        self.hexapod.move_knee(REAR_L_KNEE, 0.3, 0)
        self.hexapod.move_knee(REAR_R_KNEE, 0.3, sleep_action)
        self.hexapod.move_knee(MIDD_L_KNEE, 0.3, 0)
        self.hexapod.move_knee(MIDD_R_KNEE, 0.3, sleep_action)

        self.hexapod.move_vert(MIDD_L_VERT, 0.4, 0)
        self.hexapod.move_vert(MIDD_R_VERT, 0.4, sleep_action)
        self.hexapod.move_vert(FRON_L_VERT, 0.4, 0)
        self.hexapod.move_vert(FRON_R_VERT, 0.4, sleep_action)
        self.hexapod.move_vert(REAR_L_VERT, 0.4, 0)
        self.hexapod.move_vert(REAR_R_VERT, 0.4, sleep_action)

        self.hexapod.move_knee(FRON_L_KNEE, 0.5, 0)
        self.hexapod.move_knee(FRON_R_KNEE, 0.5, sleep_action)
        self.hexapod.move_knee(REAR_L_KNEE, 0.5, 0)
        self.hexapod.move_knee(REAR_R_KNEE, 0.5, sleep_action)
        self.hexapod.move_knee(MIDD_L_KNEE, 0.5, 0)
        self.hexapod.move_knee(MIDD_R_KNEE, 0.5, sleep_timing)

    def demo_wave(self, sleep_action, sleep_timing):
        self.hexapod.move_vert(FRON_R_VERT, 1, 0)
        self.hexapod.move_knee(FRON_R_KNEE, 1, sleep_action)
        try:
            while True:
                self.hexapod.move_knee(FRON_R_KNEE, 1, sleep_action)
                self.hexapod.move_knee(FRON_R_KNEE, 0, sleep_action)
        except KeyboardInterrupt:
            self.demo_stand(0, sleep_timing)

    def demo_dab(self, sleep_action, sleep_timing):
        self.hexapod.move_vert(MIDD_L_VERT, 0.6, 0)
        self.hexapod.move_vert(MIDD_R_VERT, 0.6, sleep_action)
        self.hexapod.move_hori(MIDD_L_HORI, 0.7, 0)
        self.hexapod.move_hori(MIDD_R_HORI, 0.3, sleep_action)
        self.hexapod.move_vert(MIDD_L_VERT, 0.3, 0)
        self.hexapod.move_vert(MIDD_R_VERT, 0.3, sleep_action)
        self.hexapod.move_vert(FRON_L_VERT, 0.7, 0)
        self.hexapod.move_vert(FRON_R_VERT, 0.7, sleep_action)
        self.hexapod.move_hori(FRON_L_HORI, 0.4, 0)
        self.hexapod.move_hori(FRON_R_HORI, 0.6, sleep_action)
        self.hexapod.move_knee(FRON_L_KNEE, 1, 0)
        self.hexapod.move_knee(FRON_R_KNEE, 0, sleep_action)
        self.hexapod.move_vert(FRON_L_VERT, 0.7, 0)
        self.hexapod.move_vert(FRON_R_VERT, 0.3, sleep_action)

        self.hexapod.wait_interrupt(message="waiting for dab end")
        self.hexapod.move_vert(FRON_R_VERT, 1, sleep_timing + 0.5)
        self.hexapod.move_vert(FRON_L_VERT, 0.4, 0)
        self.hexapod.move_knee(FRON_L_KNEE, 0.5, 0)
        self.hexapod.move_knee(FRON_R_KNEE, 0.5, sleep_action)
        self.hexapod.move_vert(FRON_R_VERT, 0.5, sleep_timing)
        self.hexapod.move_vert(MIDD_L_VERT, 0.6, 0)
        self.hexapod.move_vert(MIDD_R_VERT, 0.6, sleep_action + 0.25)
        self.hexapod.move_hori(MIDD_L_HORI, 0.5, 0)
        self.hexapod.move_hori(MIDD_R_HORI, 0.5, sleep_action)
        self.hexapod.move_vert(MIDD_L_VERT, 0.4, 0)
        self.hexapod.move_vert(MIDD_R_VERT, 0.4, sleep_timing)
