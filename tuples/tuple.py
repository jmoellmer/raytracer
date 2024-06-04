from globals import EPS

class Tuple:

    def __init__(self, x, y, z, w):
        self.x, self.y, self.z, self.w = x, y, z, w

    def __repr__(self):
        return f"Tuple({self.x:.4f}, {self.y:.4f}, {self.z:.4f}, {self.w:.4f})"
    
    def __str__(self):
        return f"({self.x:.4f}, {self.y:.4f}, {self.z:.4f}, {self.w:.4f})"
    
    def __eq__(self, o):
        return eq(self.x, o.x) and eq(self.y, o.y) and eq(self.z, o.z) and eq(self.w, o.w)

    def __add__(self, o):
        return Tuple(self.x + o.x, self.y + o.y, self.z + o.z, self.w + o.w)

    def __sub__(self, o):
        return Tuple(self.x - o.x, self.y - o.y, self.z - o.z, self.w - o.w)
    
    def __neg__(self):
        return Tuple(-self.x, -self.y, -self.z, -self.w)

    def __mul__(self, n):
        return Tuple(self.x * n, self.y * n, self.z * n, self.w * n)

    def __rmul__(self, n):
        return Tuple(n * self.x, n * self.y, n * self.z, n * self.w)
    
    def __truediv__(self, n):
        return Tuple(self.x / n, self.y / n, self.z / n, self.w / n)

def eq(a, b):
    return abs(a - b) < EPS