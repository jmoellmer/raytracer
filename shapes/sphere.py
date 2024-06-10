from tuples.point import Point

import uuid

class Sphere:
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
        self._id = uuid.uuid4()
        self.radius = radius
        self.center = center

    @property
    def id(self):
        """Unique id of a sphere. This is a caluclated property, 
        giving read-only access to the id
        
        Returns
        -------
        uuid
            The unique id of the sphere
        """
        return self._id

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
