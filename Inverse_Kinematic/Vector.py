import math
import inspect
from Point import Point

import math


class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def heading(self):
        angle = math.atan2(self.x, self.y) * 18
        return angle

    def __sub__(self, v2):
        x = self.x - v2.x
        y = self.y - v2.y
        return Vector(x, y)

    def __add__(self, v2):
        x = self.x + v2.x
        y = self.y + v2.y
        return Vector(x, y)

    def __str__(self):
        return f"x/y : ({round(self.x, 2)}/{round(self.y, 2)})"
