from matrices.matrix import Matrix
from tuples.tuple import Tuple

def main():
    # What happens when you invert the identity matrix?
    I = Matrix.identity(4)
    print(f"I^-1:\n{I.inverse()}")

    # What happens when you multiply a matrix by its inverse?
    A = Matrix([[-5, 2, 6, -8],
               [1, -5, 1, 8],
               [7, 7, -6, -7],
               [1, -3, 7, 4]])
    
    print(f"A*A^-1:\n {A * A.inverse()}")

    print(f"AT^-1\n{A.transpose().inverse()}")
    print(f"A^-1T\n{A.inverse().transpose()}")

    I[2, 3]=42
    t0 = Tuple(2, 2, 2, 1)
    t1 = I * t0
    print(f"I'*t1={t1}")

if __name__ == "__main__":
    main()