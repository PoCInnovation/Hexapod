from Segment import Segment
from Leg import Leg
import tkinter as tk

class Drawer:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Reverse Kinematic")
        self.can = tk.Canvas(self.root, width=600, height=600,
            bg="black", highlightthickness=0)
        self.can.pack()
        self.root.bind_all("<Escape>", self.quit)
        self.can.bind('<Motion>', self.handle_mouse_motion)

        # leg
        self.leg = Leg()
        self.draw_leg()

    def run(self):
        self.root.mainloop()

    def redraw(self):
        self.can.delete("all")
        self.draw_leg()

    def handle_mouse_motion(self, event):
        x = event.x
        y = event.y
        self.leg.head_to(x, y)
        self.redraw()

    def quit(self, event=None):
        self.root.quit()
        self.root.destroy()

    def draw_leg(self):
        colors = ['red', 'blue', 'yellow']
        segments = self.leg.get_segments()

        for i, segment in enumerate(segments):
            # A little circe to show the base
            self.can.create_line(
                segment.p1.x, segment.p1.y,
                segment.p2.x, segment.p2.y,
                fil="green", width=6
            )

            self.can.create_oval(
                segment.p1.x - 10, segment.p1.y - 10,
                segment.p1.x + 10, segment.p1.y + 10,
                fill=colors[i]
            )



