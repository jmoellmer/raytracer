class Intersection:
    def __init__(self, t, o):
        """An intersection encapsulates the distance from the ray origin to the intersection point
        
        Parameters
        ----------

        t : float
            The distance from the ray origin to the intersection point

        o : geometric object
            The object that was intersected
        """
        self._t = t
        self._o = o

    @property
    def t(self):
        """The distance from the ray origin to the intersection point
        
        Returns
        -------
        t : float
            The distance from the ray origin to the intersection point
        """
        return self._t
    
    @property
    def object(self):
        """The object that was intersected
        
        Returns
        -------
        o : geometric object
            The object that was intersected
        """
        return self._o
    
    @staticmethod
    def hit(xs):
        """Given a list of intersections, return the intersection with the smallest non-negative t value
        
        Parameters
        ----------
        xs : list
            A list of intersections
            
        Returns
        -------
        Intersection
            The intersection with the smallest non-negative t value
        """
        if len(xs) == 0:
            return None
        else:
            valid_hits = sorted((x for x in xs if x.t >= 0), key=lambda x: x.t)
            return valid_hits[0] if valid_hits else None