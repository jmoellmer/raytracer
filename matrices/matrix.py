from globals import EPS

from tuples.tuple import Tuple
from tuples.vector import dot

import copy

class Matrix:

    def __init__(self, matrix=None, rows=0, cols=0, default=0):
        if matrix == None:
            self._M = [[default for _ in range(cols)] for _ in range(rows)]
        else:
            self._M = matrix
        self._rows = len(self._M)
        self._cols = len(self._M[0])
        self.iter_by_cols = False

    def __len__(self):
        return len(self._M)

    def __getitem__(self, index):
        if isinstance(index, tuple):
            row, col = index
            return self._M[row][col] # return element
        elif isinstance(index, int):
            return self._M[index] # return row
        else:
            raise TypeError
    
    def __setitem__(self, index, value):
        if isinstance(index, tuple):
            row, col = index
            self._M[row][col] = value # set element
        elif isinstance(index, int):
            self._M[index] = value # set row
        else:
            raise TypeError

    def __str__(self):
        return '\n'.join([' '.join(f"{value:.5f}" for value in row) for row in self._M])
    
    def __eq__(self, M):
        if not self._same_shape(self._M, M):
            raise IndexError("Matrices are different shapes.")
        
        return all( # all rows ~ equal
            all(abs(a - b) <= EPS for a, b in zip(row1, row2)) # all elements are ~ equal
            for row1, row2 in zip(self._M, M)
        )

    def __iter__(self):
        if self.iter_by_cols:
            for col in range(self._cols):
                yield [self._M[row][col] for row in range(self._rows)]
        else:
            for row in self._M:
                yield row

    def _same_shape(self, A, B):
        if len(A) != len(B) or any(len(row1) != len(row2)
                                   for row1, row2 in zip(A, B)):
            return False
        return True
    
    def __mul__(self, B):
        if isinstance(B, Matrix):
            return self.multiply_matrices(B)
        elif isinstance(B, Tuple):
            return self.multiply_by_tuple(B)
        else:
            raise TypeError

    def multiply_matrices(self, B):
        B.iter_by_cols = True
        result = [
            [
                sum(a * b for a,b in zip(row, col)) 
                for col in B
            ]
            for row in self._M
        ]
        return Matrix(result)
    
    def multiply_by_tuple(self, b):
        result = [dot(Tuple(*row), b) for row in self._M]
        return Tuple(*result)
    
    @classmethod
    def identity(cls, size):
        I = [[1 if row == col else 0 for col in range(size)] for row in range(size)]
        return Matrix(I)
    
    def transpose(self):
        AT = [[self._M[row][col] for row in range(self._rows)] for col in range(self._cols)]
        return Matrix(AT)
    
    def submatrix(self, row_num, col_num):
        if row_num < 0 or row_num > self._rows or col_num < 0 or col_num > self._cols:
            raise IndexError
        
        submatrix_data = [            
            [self._M[i][j] for j in range(self._cols) if j != col_num]
            for i in range(self._rows) if i != row_num
        ]
        return Matrix(submatrix_data)

    def determinant(self):
        if self._rows != self._cols:
            raise ValueError("Matrix is not square")
        
        if self._rows == 2:
            return self._M[0][0] * self._M[1][1] - self._M[0][1] * self._M[1][0]
        else:
            d = 0
            for j in range(self._cols):
                d += self._M[0][j] * self.cofactor(0, j)
            return d

    def minor(self, row_num, col_num):
        S = self.submatrix(row_num, col_num)
        return S.determinant()
    
    def cofactor(self, row_num, col_num):
        m = self.minor(row_num, col_num)
        if (row_num + col_num) % 2 == 0:
            return m
        else:
            return -m
        
    def inverse(self):
        if self.determinant() == 0:
            raise ValueError("Matrix is not invertable")
       
        X = Matrix(None, self._rows, self._cols)
        d = self.determinant() 
       
        for i in range(self._rows):
            for j in range(self._cols):
                c = self.cofactor(i, j)
                X[j, i] = c / d
        
        return X