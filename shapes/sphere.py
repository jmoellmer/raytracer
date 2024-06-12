from shapes.shape import Shape
from tuples.point import Point

class Sphere(Shape):
    def __init__(self, radius, center):
        """A default sphere origin (center point) at the world origin (0, 0, 0).
        A default radius of 1.0, unit sphere.

        Parameters
        ----------
        radius : float
            The radius of the sphere

        center : Point
            The center point of the sphere
        """
        super().__init__()
        self.radius = radius
        self.center = center

class SphereFactory:

    @staticmethod
    def sphere(radius=1.0, center=Point(0, 0, 0)):
        """Creates a sphere with the given radius and center point
        
        Parameters
        ----------
        radius : float
            The radius of the sphere

        center : Point
            The center point of the sphere

        Returns
        -------
        Sphere
            A sphere object
        """
        return Sphere(radius, center)
