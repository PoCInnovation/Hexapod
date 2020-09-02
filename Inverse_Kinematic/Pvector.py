import math

class Pvector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def set(self, x, y):
        self.x = x
        self.y = y

    def __sub__(self, p2):
        new_x = self.x - p2.x
        new_y = self.y - p2.y
        return Pvector(new_x, new_y)

    def __mult__(self, n):
        self.x *= n
        self.y *= n

    def heading(self):
        return math.atan2(self.y, self.x)

    def __str__(self):
        return f"x : {self.x} y : {self.y}"