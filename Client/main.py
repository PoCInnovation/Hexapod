#!/usr/bin/env python3

import hardcoded_movements
import sys
from constants import *
from hexapod_connection import *
from tkinter import *
from values import *

ENGINES_GUI = {
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

GUI_COLOR = "#E4E4E4"

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
            self.btn[i].grid(column=1 + i, row=row, pady=5, padx=5)

    def get(self):
        return self.var.get()

    def disable(self):
        for i in self.btn:
            i.config(state='disable')

    def enable(self):
        for i in self.btn:
            i.config(state='normal')


class Gui:
    def __init__(self, port=None):
        self.connection = HexapodConnection(port)
        self.hardcoded_movements = hardcoded_movements.HardcodedMovements(self.connection)
        self.setup_window()

    def change_engine(self, Event=None):
        self.set_angle_equivalent()
        engine = self.get_selected_engine()
        min_max = get_engine_min_max(engine)
        self.min.set(min_max[MIN])
        self.max.set(min_max[MAX])

    def place_engines_frame(self):
        self.engine_frame = LabelFrame(self.testing_frame, pady=2, text='Engine :', labelanchor='nw')
        self.btn_side = RadiobuttonGroup(['l', 'r'], ['Left ', 'Right '], 'l', 1, self.engine_frame, self.change_engine)
        self.btn_zone = RadiobuttonGroup(['f', 'm', 'r'], ['Front', 'Middle', 'Rear'], 'f', 2, self.engine_frame, self.change_engine)
        self.btn_type = RadiobuttonGroup(['k', 'v', 'h'], ['Knee ', 'Verti ', 'Hori'], 'k', 3, self.engine_frame, self.change_engine)

        self.type_all = IntVar()
        self.btn_all = Checkbutton(self.engine_frame, text="All type", variable=self.type_all, command=self.disable_toggle)
        self.btn_all.grid(row=3, column=5)

        self.live_var = IntVar()
        self.btn_live = Checkbutton(self.engine_frame, text="Live", variable=self.live_var, command=self.change_send_btn_state)
        self.btn_live.grid(row=3, column=6)

        self.engine_frame.grid(row=1, column=1)

    def place_history_frame(self):
        self.history_frame = LabelFrame(self.testing_frame, pady=2, text="History", labelanchor='nw')
        self.history_listbox = Listbox(self.history_frame, width=55)
        self.history_listbox.grid(column=1, row=1, rowspan=6)
        self.edit_history_var = 0
        self.sleep_time_history = DoubleVar()
        self.sleep_time_history.set(1)
        self.scale_sleep_time_history = Scale(self.history_frame, orient='vertical', \
                                              from_=0, to=2, resolution=0.2, tickinterval=0.2, variable=self.sleep_time_history, length=200)
        self.scale_sleep_time_history.grid(row=1, column=3, rowspan=12)
        Button(self.history_frame, text="play", padx=20, command=self.play_history_item).grid(column=2,row=1)
        Button(self.history_frame, text="play all", padx=10, command=self.play_all_history).grid(column=2,row=2)
        self.btn_edit_history = Button(self.history_frame, text="edit", padx=20, command=self.edit_history_item)
        self.btn_edit_history.grid(column=2,row=3)
        Button(self.history_frame, text="delete", padx=14, command=self.delete_history_item).grid(column=2,row=4)
        Button(self.history_frame, text="clear", padx=17, command=self.clear_history).grid(column=2,row=5)
        self.history_frame.grid(row=1, column=2)

    def get_selected_history_item(self):
        try:
            item = self.history_listbox.get(self.history_listbox.curselection())
            return item
        except:
            return None

    def play_all_history(self):
        history = self.history_listbox.get(0, END)
        for i in history:
            command = i.split()[-1]
            self.connection.send_command(command, 0)
            time.sleep(self.sleep_time_history.get())

    def play_history_item(self):
        item = self.get_selected_history_item()
        if item != None:
            command = item.split()[-1]
            self.connection.send_command(command, 0)

    def edit_history_item(self):
        item = self.get_selected_history_item()
        if item == None:
            return
        if self.edit_history_var == 0:
            self.btn_edit_history.config(bg='red', activebackground='red')
            self.btn_send.config(text='Ok')
            self.edit_history_var = 1
        else:
            self.btn_edit_history.config(bg='#d9d9d9', activebackground='#ececec')
            self.btn_send.config(text='send')
            self.edit_history_var = 0

    def clear_history(self):
        self.history_listbox.delete(0, END)

    def delete_history_item(self):
        try:
            item = self.history_listbox.curselection()
            self.history_listbox.delete(item)
        except:
            pass

    def place_angle_frame(self):
        self.angle_equivalent = IntVar()
        self.angle = DoubleVar()

        self.angle.set(0.5)
        self.set_angle_equivalent()
        self.angle.trace('w', self.set_angle_equivalent)

        self.angle_frame = LabelFrame(self.testing_frame, pady=2, text='Angle :', labelanchor='nw')
        # Scale
        self.scale_angle = Scale(self.angle_frame, orient='horizontal', from_=0, to=1, \
                                 resolution=0.05, tickinterval=0.05, length=1000, variable=self.angle, command=self.send_live)
        self.scale_angle.grid(column=1, row=1, columnspan=8)
        # Entry
        self.custom_angle_ent = Entry(self.angle_frame, width=5, textvariable=self.angle)
        self.custom_angle_ent.grid(column=1, row=2)
        # Angle Equivalent
        Label(self.angle_frame, text="Angle Equivalent: ").grid(column=7, row=2)
        self.label_angle_equivalent = Label(self.angle_frame, textvariable=self.angle_equivalent)
        self.label_angle_equivalent.grid(column=8, row=2)
        self.angle_frame.grid(column=1, row=2, padx=10, pady=10, columnspan=8)

    def place_speed_frame(self):
        self.speed_frame = LabelFrame(self.testing_frame, pady=2, text='Speed :', labelanchor='nw')
        self.speed = IntVar()
        self.speed.set(1500)
        self.custom_speed_ent = Entry(self.speed_frame, width=5, textvariable=self.speed)
        self.custom_speed_ent.grid(column=1, row=2)
        self.scale_speed = Scale(self.speed_frame, orient='horizontal', from_=0, to=3000, resolution=50, tickinterval=200, length=1000, variable=self.speed)
        self.scale_speed.grid(column=1, row=1, columnspan=10)
        self.custom_general_speed = IntVar()
        self.speed_all_btn = Checkbutton(self.speed_frame, text="Actions speed", command=self.change_action_general_speed, variable=self.custom_general_speed)
        self.speed_all_btn.grid(column=10, row=2)
        self.speed_frame.grid(column=1, row=3, columnspan=8)

    def place_testing_frame(self):
        self.testing_frame = LabelFrame(self.fen, relief='sunken', pady=2, text='Testing :', labelanchor='n')
        self.place_engines_frame()
        self.place_history_frame()
        self.place_angle_frame()
        self.place_speed_frame()
        self.btn_send = Button(self.testing_frame, text="send", command=self.send)
        self.btn_send.grid(column=1, row=4 ,columnspan=8, pady=20)
        self.testing_frame.grid(column=1, row=1, padx=10)

    def place_min_max_frame(self):
        self.min_max_frame = LabelFrame(self.fen , pady=2, text='Min/Max :', relief='sunken',labelanchor='n')
        self.min = IntVar()
        self.max = IntVar()
        self.set_min_max()
        self.min_scale = Scale(self.min_max_frame, orient='vertical', from_=0, to=3000, \
                               resolution=50, tickinterval=200, length=500, label='min', variable=self.min, command=self.update_engine_min_max)
        self.min_scale.grid(column=1, row=1)
        self.max_scale = Scale(self.min_max_frame, orient='vertical', from_=0, to=3000, \
                               resolution=50, tickinterval=200, length=500, label='max', variable=self.max, command=self.update_engine_min_max)
        self.max_scale.grid(column=2, row=1)

        self.btn_save = Button(self.min_max_frame, text='save', command=self.save_custom_min_max)
        self.btn_save.grid(column=1, row=2, columnspan=2, pady=10)
        self.min_max_frame.grid(column=2, row=1, rowspan=8)

    def place_action_frame(self):
        self.action_btn_frame = LabelFrame(self.fen, bd=2, relief='sunken', pady=20, text='Actions :', labelanchor='n', padx=25)
        self.action_btn = ["sit", "stand", "stand1", "stand2", "stand3", "wave", "dab", "forward", "stop", "backward", "rotate_right", "rotate_left", "replace_legs", "test_feedback"]
        i, j = 1, 1
        for k in range(len(self.action_btn)):
            Button(self.action_btn_frame, text=self.action_btn[k], command=getattr(self.hardcoded_movements, self.action_btn[k])).grid(row=2 + j, column=i, padx=5)
            i += 1
            if i > 10:
                i = 1
                j += 1
        self.action_btn_frame.grid(row=5, column=1)

    def setup_window(self):
        self.fen = Tk()
        self.fen.option_readfile('./.tkopt')
        self.fen.configure(bg="#E4E4E4")
        self.fen.geometry("1350x700")
        self.fen.title("Hexapod Client")
        self.place_testing_frame()
        self.place_min_max_frame()
        self.place_action_frame()
        self.fen.bind_all("<Escape>", self.quit)
        self.fen.bind_all("<space>", self.send)
        self.fen.mainloop()

    def change_action_general_speed(self, Event=None):
        if self.custom_general_speed.get() == 1:
            speed = int(self.speed.get())
            self.hardcoded_movements.set_actions_speed(speed)
        else:
            self.hardcoded_movements.set_actions_speed(-1)

    def get_selected_engine(self):
        return ENGINES_GUI[self.btn_zone.get() + self.btn_side.get() + self.btn_type.get()]

    def update_engine_min_max(self, Event=None):
        engine = self.get_selected_engine()
        new_min = self.min.get()
        new_max = self.max.get()

        engine_min_max = get_engine_min_max(engine)

        set_engine_min_max(engine, new_min, new_max)
        self.set_angle_equivalent()

    def save_custom_min_max(self, evt=None):
        data = {}
        index = 0
        for i in MIN_MAX_ENGINES:
            for j in i:
                for k in j:
                    for l in k:
                        # print(INDEX_TO_ENGINE_NAME[index], l, sep="")
                        data[INDEX_TO_ENGINE_NAME[index]] = l
                        index += 1
        data = json.dumps(data, indent=4)
        print(data, file=open('constants.json', 'w'))

    def set_min_max(self):
        engine = self.get_selected_engine()
        vals = get_engine_min_max(engine)
        self.max.set(vals[MAX])
        self.min.set(vals[MIN])

    def set_angle_equivalent(self, *args):
        angle = float(self.angle.get())
        engine = self.get_selected_engine()
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

    def send_live(self, event=None):
        if self.live_var.get() == 1:
            self.send()

    def add_command_to_history(self, engine, command):
        speed = self.speed.get()
        angle = self.angle.get()
        self.history_listbox.insert(self.history_listbox.size(), \
                                    f"{ENGINES_DICT_REVERSED[engine]} : A={angle}, S={speed}, m/M="
                                    f"{self.min.get()}/{self.max.get()}    {command}")
        self.history_listbox.selection_clear(0, END)
        self.history_listbox.selection_anchor(END)
        self.history_listbox.selection_set(ANCHOR)

    def send(self, event=None):
        angle = float(self.angle.get())
        speed = int(self.speed.get())

        engine = self.get_selected_engine()
        command = ""

        if self.type_all.get() == 1:
            initial_angle = angle
            for key, value in ENGINES_GUI.items():
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
            if event != "FROM_HISTORY" and self.edit_history_var == 0:
                self.add_command_to_history(engine, command)
        if self.edit_history_var == 0:
            print(f"min : {self.min.get()} max : {self.max.get()}")
            self.connection.send_command(command, 0)
        else:
            self.edit_history_item()

    def quit(self, event=None):
        self.connection.close()
        self.fen.quit()
        self.fen.destroy()


def main(argc, argv):
    if argc == 2:
        print("Starting wired mode")
        Gui(argv[1])
    else:
        print("Specify port if you want to connect using a wire\n")
        print("Starting bluetooth mode")
        Gui()

if __name__ == '__main__':
    main(len(sys.argv), sys.argv)
