# we 
class Matrix4:
    # a matrix is defined by m X n (m is the number of rows and n the number of columns)
    # we will almost always use squared matrixes in CG
    def __init__(self):
        self.m = [
            [1, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 1]
        ]

    # also called matrix product, and results in a new matrix
    def multiply(self):
        pass
