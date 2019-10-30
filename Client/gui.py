#!/usr/bin/python3

from tkinter import*
from values import *
from hexapod_connection import*
import hardcoded_movements
import sys

ENGINES = {
    "rrh": REAR_R_HORI,
    "rrv": REAR_R_VERT,
    "rrk": REAR_R_KNEE,
    "rlh": REAR_L_HORI,
    "rlv": REAR_L_VERT,
    "rlk": REAR_L_KNEE,
    "mrh": MIDD_R_HORI,
    "mrv": MIDD_R_VERT,
    "mrk": MIDD_R_KNEE,
    "mlh": MIDD_L_HORI,
    "mlv": MIDD_L_VERT,
    "mlk": MIDD_L_KNEE,
    "frh": FRON_R_HORI,
    "frv": FRON_R_VERT,
    "frk": FRON_R_KNEE,
    "flh": FRON_L_HORI,
    "flv": FRON_L_VERT,
    "flk": FRON_L_KNEE
}

class Gui:
    def __init__(self, mode):
        self.fen = Tk()
        self.fen.geometry("1000x500")
        self.connection = HexapodConnection(mode=mode)
        self.hardcoded_movements = hardcoded_movements.HardcodedMovements(self.connection)

        # side
        self.vals_side = ['l', 'r']
        self.etiqs_side = ['Left', 'Right']
        self.side = StringVar()
        self.side.set('l')
        Radiobutton(self.fen, variable=self.side, text=self.etiqs_side[0], value=self.vals_side[0]).grid(column=1, row=1)
        Radiobutton(self.fen, variable=self.side, text=self.etiqs_side[1], value=self.vals_side[1]).grid(column=2, row=1)

        # zone
        self.vals_zone = ['f', 'm', 'r']
        self.etiqs_zone = ['Front', 'Middle', 'Rear']
        self.zone = StringVar()
        self.zone.set('f')
        Radiobutton(self.fen, variable=self.zone, text=self.etiqs_zone[0], value=self.vals_zone[0]).grid(column=1, row=2)
        Radiobutton(self.fen, variable=self.zone, text=self.etiqs_zone[1], value=self.vals_zone[1]).grid(column=2, row=2)
        Radiobutton(self.fen, variable=self.zone, text=self.etiqs_zone[2], value=self.vals_zone[2]).grid(column=3, row=2)

        # type
        self.vals_type = ['k', 'v', 'h']
        self.etiqs_type = ['Knee', 'Verti', 'Hori']
        self.type = StringVar()
        self.type.set('k')
        Radiobutton(self.fen, variable=self.type, text=self.etiqs_type[0], value=self.vals_type[0]).grid(column=1, row=3)
        Radiobutton(self.fen, variable=self.type, text=self.etiqs_type[1], value=self.vals_type[1]).grid(column=2, row=3)
        Radiobutton(self.fen, variable=self.type, text=self.etiqs_type[2], value=self.vals_type[2]).grid(column=3, row=3)

        # angle
        self.angle = DoubleVar()
        self.angle.set(0.5)
        Scale(self.fen, orient='horizontal', from_=0, to=1, resolution=0.05, tickinterval=0.05, length=800, variable=self.angle).grid(column=1, row=4, columnspan=8)

        # speed
        self.speed = IntVar()
        self.speed.set(500)
        Scale(self.fen, orient='horizontal', from_=100, to=1000, resolution=50, tickinterval=50, length=800, variable=self.speed).grid(column=1, row=5, columnspan=8)

        # Ok
        Button(self.fen, text="send", command=self.send).grid(column=1, row=6 ,columnspan=8)

        # actions
        Button(self.fen, text="sit", command=self.hardcoded_movements.sit)         .grid (row=7, column=1)
        Button(self.fen, text="stand", command=self.hardcoded_movements.stand)     .grid (row=7, column=2)
        Button(self.fen, text="stand1", command=self.hardcoded_movements.stand1)   .grid (row=7, column=3)
        Button(self.fen, text="stand2", command=self.hardcoded_movements.stand2)   .grid (row=7, column=4)
        Button(self.fen, text="stand3", command=self.hardcoded_movements.stand3)   .grid (row=7, column=5)
        Button(self.fen, text="wave", command=self.hardcoded_movements.wave)       .grid (row=7, column=6)
        Button(self.fen, text="dab", command=self.hardcoded_movements.dab)         .grid (row=7, column=7)
        Button(self.fen, text="forward", command=self.hardcoded_movements.forward) .grid (row=7, column=8)
        Button(self.fen, text="stop", command=self.hardcoded_movements.stop)       .grid (row=7, column=9)

        self.fen.bind_all("<Escape>", self.quit)
        self.fen.mainloop()

    def convert_angle(self, angle, engine, kind):
        side = engine <= 15           # We need to know which side the engine is on

        if kind == "v":
            tab_values = VERT_VALUES
        elif kind == "h":
            tab_values = HORI_VALUES
        else: # knee
            tab_values = KNEE_VALUES

        return angle * (tab_values[side][0] - tab_values[side][1]) + tab_values[side][1]

    def send(self, event=None):
        angle = float(self.angle.get())
        speed = int(self.speed.get())
        engine = ENGINES[self.zone.get() + self.side.get() + self.type.get()]

        angle = self.convert_angle(angle, engine, self.type.get())

        command = "#%dP%.0fS%d!" % (engine, angle, speed)   # Command to send
        print(command)
        self.connection.send_command(command, 0)

    def quit(self, event=None):
        self.fen.quit()
        self.fen.destroy()

if __name__ == '__main__':
    if len(sys.argv) == 2 and sys.argv[1] == "--wire":
        Gui("wire")
    else:
        Gui("wifi")
