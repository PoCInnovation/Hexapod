#!/usr/bin/python3

from tkinter import*
from tkinter import messagebox
from values import *
from hexapod_connection import*
import hardcoded_movements
import sys

ENGINES = {
    "flh": HORI_FRONT_L,
    "flk": KNEE_FRONT_L,
    "flv": VERT_FRONT_L,
    "frh": HORI_FRONT_R,
    "frk": KNEE_FRONT_R,
    "frv": VERT_FRONT_R,
    "mlh": HORI_MIDDLE_L,
    "mlk": KNEE_MIDDLE_L,
    "mlv": VERT_MIDDLE_L,
    "mrh": HORI_MIDDLE_R,
    "mrk": KNEE_MIDDLE_R,
    "mrv": VERT_MIDDLE_R,
    "rlh": HORI_REAR_L,
    "rlk": KNEE_REAR_L,
    "rlv": VERT_REAR_L,
    "rrh": HORI_REAR_R,
    "rrk": KNEE_REAR_R,
    "rrv": VERT_REAR_R
}

class RadiobuttonGroup:
    def __init__(self, vals, etiqs, default_value, row, fen, func=None):
        if len(vals) != len(etiqs):
            print("len differs")
            exit(1)
        self.var = StringVar()
        self.var.set(default_value)
        self.btn = []
        for i in range(len(vals)):
            self.btn.append(Radiobutton(fen, variable=self.var, text=etiqs[i], value=vals[i], command=func))
            self.btn[i].grid(column=1 + i, row=row)

    def get(self):
        return self.var.get()

    def disable(self):
        for i in self.btn:
            i.config(state='disable')

    def enable(self):
        for i in self.btn:
            i.config(state='normal')

class Gui:
    def __init__(self, mode):
        self.connection = HexapodConnection(mode=mode)
        self.hardcoded_movements = hardcoded_movements.HardcodedMovements(self.connection)
        self.setup_window()

    def setup_window(self):
        self.fen = Tk()
        self.fen.geometry("1280x520")
        self.fen.title("Hexapod Client")

        self.btn_side = RadiobuttonGroup(['l', 'r'], ['Left', 'Right'], 'l', 1, self.fen)
        self.btn_zone = RadiobuttonGroup(['f', 'm', 'r'], ['Front', 'Middle', 'Rear'], 'f', 2, self.fen)
        self.btn_type = RadiobuttonGroup(['k', 'v', 'h'], ['Knee', 'Verti', 'Hori'], 'k', 3, self.fen, self.set_angle_equivalent)

        # Type all
        self.type_all = IntVar()
        self.btn_all = Checkbutton(self.fen, text="All type", variable=self.type_all, command=self.disable_toggle)
        self.btn_all.grid(row=3, column=5)

        # live
        self.live_var = IntVar()
        self.btn_live = Checkbutton(self.fen, text="Live", variable=self.live_var, command=self.change_send_btn_state)
        self.btn_live.grid(row=3, column=6)

        # angle
        self.angle = DoubleVar()
        self.angle.set(0.5)
        self.angle.trace('w', self.set_angle_equivalent)
        self.custom_angle_ent = Entry(self.fen, width=5, textvariable=self.angle)
        self.custom_angle_ent.grid(column=1, row=5)
        self.scale_angle = Scale(self.fen, orient='horizontal', from_=0, to=1, resolution=0.05, tickinterval=0.05, length=800, variable=self.angle, command=self.send_live)
        self.scale_angle.grid(column=1, row=4, columnspan=8)
        self.angle_equivalent = IntVar()
        self.set_angle_equivalent()
        Label(self.fen, text="Angle Equivalent  --> ").grid(column=7, row=5)
        self.label_angle_equivalent = Label(self.fen, textvariable=self.angle_equivalent)
        self.label_angle_equivalent.grid(column=8, row=5, columnspan=2)

        self.min = IntVar()
        self.max = IntVar()
        self.set_min_max()
        self.min_scale = Scale(self.fen, orient='vertical', from_=0, to=3000, resolution=50, tickinterval=200, length=500, label='min', variable=self.min)
        self.min_scale.grid(column=10, row=1, rowspan=12)
        self.max_scale = Scale(self.fen, orient='vertical', from_=0, to=3000, resolution=50, tickinterval=200, length=500, label='max', variable=self.max)
        self.max_scale.grid(column=11, row=1, rowspan=12)

        self.btn_save = Button(self.fen, text='save', command=self.save_custom_min_max)
        self.btn_save.grid(column=12, row = 1, rowspan=12)

        # speed
        self.speed = IntVar()
        self.speed.set(1500)
        self.custom_speed_ent = Entry(self.fen, width=5, textvariable=self.speed)
        self.custom_speed_ent.grid(column=1, row=7)
        self.scale_speed = Scale(self.fen, orient='horizontal', from_=0, to=3000, resolution=50, tickinterval=200, length=800, variable=self.speed)
        self.scale_speed.grid(column=1, row=6, columnspan=8)

        # Actions
        self.action_btn_frame = Frame(self.fen)
        Label(self.action_btn_frame, text='Action :').grid(column=1, row=1)
        self.action_btn = ["sit", "stand", "stand1", "stand2", "stand3", "wave", "dab", "forward", "stop", "forward_2"]
        i, j = 1, 1
        for k in range(len(self.action_btn)):
            Button(self.action_btn_frame, text=self.action_btn[k], command=getattr(self.hardcoded_movements, self.action_btn[k])).grid(row=2 + j, column=i, padx=5)
            i += 1
            if i > 10:
                i = 1
                j += 1
        self.action_btn_frame.grid(row=9, column=1, columnspan=7)

        # Ok
        self.btn_send = Button(self.fen, text="send", command=self.send)
        self.btn_send.grid(column=1, row=10 ,columnspan=8, pady=20)

        self.fen.bind_all("<Escape>", self.quit)
        self.fen.bind_all("<space>", self.send)
        self.fen.mainloop()

    def save_custom_min_max(self, evt=None):
        engine = ENGINES[self.btn_zone.get() + self.btn_side.get() + self.btn_type.get()]
        new_min = self.min
        new_max = self.max

        print()

    def set_min_max(self):
        engine = ENGINES[self.btn_zone.get() + self.btn_side.get() + self.btn_type.get()]
        vals = get_engine_min_max(engine)
        self.max.set(vals[MAX])
        self.min.set(vals[MIN])

    def set_angle_equivalent(self, *args):
        angle = float(self.angle.get())
        engine = ENGINES[self.btn_zone.get() + self.btn_side.get() + self.btn_type.get()]
        self.btn_type.get()
        val = convert_angle(angle, engine)
        self.angle_equivalent.set(val)

    def disable_toggle(self):
        if self.type_all.get() == 1:
            self.btn_side.disable()
            self.btn_zone.disable()
        else:
            self.btn_side.enable()
            self.btn_zone.enable()

    def change_send_btn_state(self):
        if self.live_var.get() == 1:
            self.btn_send.config(state='disable')
        else:
            self.btn_send.config(state='normal')

    def angle_to_ratio(self, angle, engine, kind):
        side = engine <= 15   # We need to know which side the engine is on
        if kind == "v":
            vals = VERT_VALUES
        elif kind == "h":
            vals = HORI_VALUES
        else: # k
            vals = KNEE_VALUES
        return (angle - vals[side][1]) / (vals[side][0] - vals[side][1])

    def send_live(self, event=None):
        if self.live_var.get() == 1:
            self.send()

    def send(self, event=None):
        angle = float(self.angle.get())
        speed = int(self.speed.get())

        engine = ENGINES[self.btn_zone.get() + self.btn_side.get() + self.btn_type.get()]
        command = ""

        if self.type_all.get() == 1:
            initial_angle = angle
            for key, value in ENGINES.items():
                if self.btn_type.get() not in key:
                    continue
                angle = convert_angle(initial_angle, value)
                if command != "":
                    command += " "
                command += "#%dP%.0fS%d" % (value, angle, speed)
            command += '!'
        else:
            angle = convert_angle(angle, engine)
            command = "#%dP%.0fS%d!" % (engine, angle, speed)   # Command to send
        self.connection.send_command(command, 0)

    def quit(self, event=None):
        self.fen.quit()
        self.fen.destroy()

if __name__ == '__main__':
    if len(sys.argv) == 2 and sys.argv[1] == "--wire":
        Gui("wire")
    else:
        print("Use --wire if you want to connect using a wire\n")
        Gui("wifi")
