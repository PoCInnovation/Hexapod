from Segment import Segment

import tkinter as tk


class Drawer:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Reverse Kinematic")

        self.can = tk.Canvas(self.root, width=600, height=600, bg="black",
                             highlightthickness=0)
        self.can.pack()

        self.root.bind_all("<Escape>", self.quit)
        self.can.bind('<Motion>', self.handle_mose_motion)

        self.segment = Segment(300, 300, 100)
        self.segment.draw(self.can)

    def run(self):
        self.root.mainloop()

    def redraw(self):
        self.can.delete("all")
        self.segment.draw(self.can)

    def handle_mose_motion(self, event):
        x = event.x
        y = event.y
        self.segment.head_to(x, y)
        self.redraw()

    def quit(self, event=None):
        self.root.quit()
        self.root.destroy()
