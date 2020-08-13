from Pvector import Pvector

import math


class Segment:
    def __init__(self, x, y, length, angle=0):
        self.p1 = Pvector(x, y)
        self.p2 = Pvector()
        self.angle = angle
        self.length = length
        self.__compute_p2()

    def __compute_p2(self):
        dx = self.length * math.cos(self.angle)
        dy = self.length * math.sin(self.angle)
        self.p2.set(self.p1.x + dx, self.p1.y + dy)

    def update(self):
        self.__compute_p2()

    def __compute_segment_vector(self):
        return self.p2 - self.p1


    def follow(self, tx, ty):
        target = Pvector(tx, ty)
        direction = target - self.p1
        self.angle = direction.heading()
        self.__compute_p2()
        print(direction)
        print(self.angle)
