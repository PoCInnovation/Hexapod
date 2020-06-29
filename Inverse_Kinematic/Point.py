from dataclasses import dataclass

@dataclass
class Point:
    x: int
    y: int

    def __sub__(self, p2):
        x = self.x - p2.x
        y = self.y - p2.y
        return Point(x, y)
