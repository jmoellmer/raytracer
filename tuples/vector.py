from math import sqrt
from .tuple import Tuple

class Vector(Tuple):

    def __init__(self, x, y, z):
        super().__init__(x, y, z, 0.0)

    def __repr__(self):
        return f"Vector({self.x}, {self.y}, {self.z})"
    
def is_vector(v):
    return v.w == 0.0

def magnitude(v):
    return sqrt(v.x**2 + v.y**2 + v.z**2 + v.w**2)

def norm(v):
    length = magnitude(v)
    return Tuple(v.x / length, v.y / length, v.z / length, v.w / length)

def dot(a, b):
    return a.x * b.x + a.y * b.y + a.z * b.z + a.w * b.w

def cross(a, b):
    return Vector(a.y * b.z - a.z * b.y,
                  a.z * b.x - a.x * b.z,
                  a.x * b.y - a.y * b.x)