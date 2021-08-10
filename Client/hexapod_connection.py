from values import *
from enum import Enum

class ConType(Enum):
    SERIAL = 1
    BLE = 2

class HexapodConnection:
    """
    Class helping with hardware communication
    Compatible with wired/wireless
    """

    def __init__(self, serial_port):
        self.con_type = None

        if self.serial_port == None:
            self.con_type = ConType.SERIAL
            # init ble con
            pass
        else:
            self.con_type = ConType.BLE
            # init serial con
            pass

    def close(self):
        if self.con_type == ConType.BLE:
            # close ble
            pass
        else:
            # close serial
            pass

    def send_command(self, command, sleep_time=0):
        if self.con_type == ConType.BLE:
            # send with ble
            pass
        else:
            # send with serial
            pass
