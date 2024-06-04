from .matrix import Matrix

class Transform:

    @classmethod
    def translate(cls, x, y, z):
        """translate is a transformation that moves a point.

        If you take the inverse of a translation matrix, you
        get another translation matrix that moves a point in
        reverse. Multiplying a translation matrix by a vector
        should not change a vector.

        Parameters
        ----------
        x : float
            Amount to translate in the x-direction
        y : float
            Amount to translate in the y-direction
        z : float
            Amount to translate in the z-direction
        

        Returns
        -------
        Matrix
            A 4x4 translation matrix
        """
        return Matrix([[1, 0, 0, x],
                       [0, 1, 0, y],
                       [0, 0, 1, z],
                       [0, 0, 0, 1]])
    
    @classmethod
    def scale(cls, x, y, z):
        """Scale "moves" by multiplication, scaling all points
        on the object, effectively making it larger or smaller.

        Parameters
        ----------
        x : float
            Amount to scale x
        y : float
            Amount to scale y
        z : float
            amount to scale z
        
        Returns
        -------        
        Matrix
            A 4x4 scaling matrix
        """
        return Matrix([[x, 0, 0, 0],
                       [0, y, 0, 0],
                       [0, 0, z, 0],
                       [0, 0, 0, 1]])