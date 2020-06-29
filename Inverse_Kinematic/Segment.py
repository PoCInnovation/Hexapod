from Vector import Vector
from Point import Point

import math


class Segment:
    def __init__(self, x, y, width, angle=0):
        self.p1 = Point(x, y)
        self.width = width
        self.angle = angle
        self.p2 = None
        self.__compute_p2()

    def __compute_p2(self):
        dx = self.width * math.cos(self.angle)
        dy = self.width * math.sin(self.angle)
        self.p2 = Point(self.p1.x + dx, self.p1.y + dy)
        print(self.p2)

    def __compute_segment_vector(self):
        return self.p2 - self.p1


    def draw(self, canvas):
        canvas.create_line(
            self.p1.x,
            self.p1.y,
            self.p2.x,
            self.p2.y,
            fil="green",
            width=6
        )

        # A little circe to show the base
        canvas.create_oval(
            self.p1.x - 10,
            self.p1.y - 10,
            self.p1.x + 10,
            self.p1.y + 10,
            fill="red"
        )

    def head_to(self, x, y):
        mouse = Vector(x, y)
        vec_to_mouse = Point(mouse.x, mouse.y) - self.p1
        vec_to_mouse = Vector(vec_to_mouse.x, vec_to_mouse.y)
        self.angle = vec_to_mouse.heading()
        print(self.angle)
        self.__compute_p2()
        # self.p2.x = math.cos(self.angle * self.p1.x) - math.sin(self.angle * self.p1.y)
        # self.p2.y = math.cos(self.angle * self.p1.y) + math.sin(self.angle * self.p1.x)
        # self.p2.y = math.sin(self.angle)
        # print(self.angle, "C")
