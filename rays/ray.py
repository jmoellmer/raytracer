from tuples.vector import dot
from rays.intersection import Intersection
from shapes.sphere import Shape

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
        transformed_ray = self.transform(sphere.transform.inverse())
        sphere_to_ray = transformed_ray.origin - sphere.center
        
        a = dot(transformed_ray.direction, transformed_ray.direction)     # D**2
        b = 2 * dot(transformed_ray.direction, sphere_to_ray)  # 2OD
        c = dot(sphere_to_ray, sphere_to_ray) - 1   # O**2 - R**2

        discriminant = b**2 - 4 * a * c

        if discriminant < 0:
            return []
        
        t1 = (-b - sqrt(discriminant)) / (2 * a)
        t2 = (-b + sqrt(discriminant)) / (2 * a)
    
        return [Intersection(t1, sphere), 
                Intersection(t2, sphere)]
    
    def transform(self, matrix):
        """Transforms the ray by the given matrix
        
        Parameters
        ----------
        matrix : Matrix
            The matrix to transform the ray by

        Returns
        -------
        Ray
            The transformed ray
        """
        return Ray(matrix * self.origin, matrix * self.direction)