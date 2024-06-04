from .tuple import Tuple

class Point(Tuple):

    def __init__(self, x, y, z):
        super().__init__(x, y, z, 1.0)

    def __repr__(self):
        return f"Point({self.x}, {self.y}, {self.z})"

def is_point(p):
    return p.w == 1.0