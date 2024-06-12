import uuid

from matrices.matrix import Matrix

class Shape:
    def __init__(self):
        self._id = uuid.uuid4()
        self._transform = Matrix.identity(4)

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
    
    @property
    def transform(self):
        """The transformation matrix of the sphere
        
        Returns
        -------
        Matrix
            The transformation matrix of the sphere
        """
        return self._transform
    
    @transform.setter
    def transform(self, matrix):
        """Sets the transformation matrix of the sphere
        
        Parameters
        ----------
        matrix : Matrix
            The transformation matrix to set
        """
        self._transform = matrix