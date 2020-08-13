from Segment import Segment

class Leg:
    def __init__(self):
        self.segments = [Segment(x=300, y=300, length=100)]

    def get_segments(self):
        return self.segments

    def head_to(self, tx, ty):
        for seg in self.segments:
            seg.follow(tx, ty)
