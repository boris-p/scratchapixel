from __future__ import annotations


class Matrix4:

    IDENTITY_MATRIX = [
        [1, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1]
    ]

    # a matrix defines in a concise way, a combination of linear transformations
    # that can be applied to points and vectors (scale, rotation, translation)

    # It is defined by m X n (m is the number of rows and n the number of columns)
    # we will almost always use squared matrixes in CG

    #  a matrix multiplication is a way of combining in one matrix the effect of two other matrices
    # let's say we want to transform a point from A to B using matrix m1 and then from B to C
    # using m2, multiplying m1 with m2 gives us m3.

    # We can also get from A to C using any other point like D, and with two other Matrixes
    # m4 (a-> d) and m5 (d -> c), the resulting matrix m4*m5 will be the same m3
    #
    # Matrixes can only be multiplies if the number of columns in one is the same and the number
    # of rows in the other -
    # A 4x2 and 2x3 matrices can be multiplied and will give a 4x3 matrix. The multiplication of two 4x4 matrices gives a 4x4 matrix

    # *this rule isn't so important for us because we will almost always use 4x4 matrix so we generally won't care about whether matrices can be multiplied or not
    def __init__(self):
        self.m = self.IDENTITY_MATRIX

    # also called matrix product, and results in a new matrix
    # Matrix multiplication indeed is not commutative. M1*M2 doesn't give the same result than M2*M1
    def multiply(self, matrix: Matrix4) -> Matrix4:
        res_m = Matrix4()
        m1 = self.m
        m2 = matrix.m

        for i in range(4):
            for j in range(4):
                res_m.m[i][j] = \
                    m1[i][0] * m2[0][j] + \
                    m1[i][1] * m2[1][j] + \
                    m1[i][2] * m2[2][j] + \
                    m1[i][3] * m2[3][j]
        return res_m
