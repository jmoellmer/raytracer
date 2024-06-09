from .matrix import Matrix

from math import sin, cos

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
    
    @classmethod
    def rotate_x(cls, r):
        """Rotates r radians around the x-axis
        
        Parameters
        ----------
        r : float
            radians to rotate

        Returns
        -------
        Matrix
            A 4x4 rotation matrix
        """
        return Matrix([[1, 0, 0, 0],
                       [0, cos(r), -sin(r), 0],
                       [0, sin(r), cos(r), 0],
                       [0, 0, 0, 1]])
    
    @classmethod
    def rotate_y(cls, r):
        """Rotates r radians around the y-axis
        
        Parameters
        ----------
        r : float
            radians to rotate

        Returns
        -------
        Matrix
            A 4x4 rotation matrix
        """
        return Matrix([[cos(r),  0, sin(r), 0],
                       [0,       1, 0, 0],
                       [-sin(r), 0, cos(r), 0],
                       [0,       0, 0, 1]])
    
    @classmethod
    def rotate_z(cls, r):
        """Rotates r radians around the z-axis
        
        Parameters
        ----------
        r : float
            radians to rotate

        Returns
        -------
        Matrix
            A 4x4 rotation matrix
        """
        return Matrix([[cos(r), -sin(r), 0, 0],
                       [sin(r), cos(r), 0, 0],
                       [0, 0, 1, 0],
                       [0, 0, 0, 1]])
    
    @classmethod
    def shear(cls, x_y, x_z, y_x, y_z, z_x, z_y):
        """Shear is a transformation that slides a point in one
        direction, keeping the other two coordinates the same.

        Parameters
        ----------
        x_y : float
            x moved in proportion to y
        x_z : float
            x moved in proportion to z
        y_x : float
            y moved in proportion to x
        y_z : float
            y moved in proportion to z
        z_x : float
            z moved in proportion to x
        z_y : float
            z moved in proportion to y

        Returns
        -------
        Matrix
            A 4x4 shear matrix
        """
        return Matrix([[1, x_y, x_z, 0],
                       [y_x, 1, y_z, 0],
                       [z_x, z_y, 1, 0],
                       [0, 0, 0, 1]])
        
