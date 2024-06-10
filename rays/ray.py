from tuples.point import Point
from tuples.vector import Vector, dot
from .intersection import Intersection

from math import sqrt

class Ray:
    def __init__(self, origin, direction):
        """A ray is a line that starts at a point called the origin, 
        and a vector called the direction which says where it points.

        Parameters
        ----------
        origin : Point
            The starting point of the ray

        direction : Vector
            The direction the ray points
        """
        self.origin = origin
        self.direction = direction

    def position(self, t):
        """Computes the point at the given distance t along the ray

        Parameters
        ----------
        t : float
            The distance from the origin to the point

        Returns
        -------
        Point
            The position of the point along the ray
        """
        return self.origin + self.direction * t
    
    def intersect(self, sphere):
        """Computes the intersection of a ray with a sphere
        
        Parameters
        ----------
        sphere : Sphere
            The sphere to intersect with the ray

        Returns
        -------
        list : float
            A list of distances from the origin to the intersection points
        """
        sphere_to_ray = self.origin - sphere.center
        
        a = dot(self.direction, self.direction)     # D**2
        b = 2 * dot(self.direction, sphere_to_ray)  # 2OD
        c = dot(sphere_to_ray, sphere_to_ray) - 1   # O**2 - R**2

        discriminant = b**2 - 4 * a * c

        if discriminant < 0:
            return []
        
        t1 = (-b - sqrt(discriminant)) / (2 * a)
        t2 = (-b + sqrt(discriminant)) / (2 * a)
    
        return [Intersection(t1, sphere), 
                Intersection(t2, sphere)]