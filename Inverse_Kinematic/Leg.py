from Segment import Segment

class Leg:
    def __init__(self):
        self.segments = [
            Segment(x=600, y=500, length=150),
            Segment(x=750, y=500, length=150),
            Segment(x=900, y=500, length=150)
            ]

    def get_segments(self):
        return self.segments

    def head_to(self, tx, ty):
        for seg in self.segments:
            seg.follow(tx, ty)
