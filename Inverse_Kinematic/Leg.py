from Segment import Segment

class Leg:
    def __init__(self):
        self.segments = [
            Segment(x=600, y=500, length=150),
            # Segment(x=750, y=500, length=150),
            # Segment(x=900, y=500, length=150)
            ]

    def get_segments(self):
        return self.segments

    def head_to(self, tx, ty):
        lastx = -1
        lasty = -1
        for seg in self.segments:
            if lastx != -1 and lasty != -1:
                seg.p1.x = lastx
                seg.p1.y = lasty
            seg.follow(tx, ty)
            lastx = seg.p2.x
            lasty = seg.p2.y