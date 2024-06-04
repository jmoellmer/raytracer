from .tuple import Tuple

class Color(Tuple):

    def __init__(self, r, g, b):
        super().__init__(r, g, b, 0.0)

    def __mul__(self, o):
        if isinstance(o, Color):
            return Color(self.x * o.x, self.y * o.y, self.z * o.z)
        else:
            return super().__mul__(o) # multiply Color by a scalar

    @property
    def r(self):
        return self.x
    
    @r.setter
    def r(self, value):
        self.x = value

    @property
    def g(self):
        return self.y
    
    @g.setter
    def g(self, value):
        self.y = value

    @property
    def b(self):
        return self.z
    
    @b.setter
    def b(self, value):
        self.b = value