from __future__ import annotations
from src.geometry.Matrix4 import Matrix4
import math


class Vector3:

    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def length(self):
        return math.sqrt(self.x * self.x + self.y * self.y + self.z * self.z)

    def duplicate(self):
        return Vector3(self.x, self.y, self.z)

    # a normalized vector is a vector whose length is 1, also called a unit vector
    def normalize(self):
        vec_length = self.length()

        if vec_length > 0:
            inv_lev = 1 / vec_length
            self.x = self.x * inv_lev
            self.y = self.y * inv_lev
            self.z = self.z * inv_lev

    # this can be seen as the projection of one vector A over vector B
    # the dot product is denoted by A . B, can also be written as < A,B >
    # and consists of multiplying each element of the A vector with the
    # vector B coutnerpart
    # when the vectors generally points in the same direction their dot product is positive
    # if they are in 90% angle it's 0 and if they're in the general opposite direction
    # the dot product will be negative
    # a really interesting deeper perspective can be found here - https://www.youtube.com/watch?v=LyGKycYT2v0&vl=zh&ab_channel=3Blue1Brown
    def dot(self, v: Vector3):
        return self.x * v.x + self.y * v.y + self.z * v.z

    # get the angle to another vector
    def angle(self, v: Vector3):
        a = self.duplicate()
        a.normalize()

        b = v.duplicate()
        b.normalize()

        return math.acos(a.dot(b))

    # differently from the dot product, the cross product returns a vector
    # a vector that is perpendicular to the other two
    # written in the following syntax C= A X B
    # here (as opposed to with the dot product) the order of A and B does matter ( in defining the direction of the angle)
    # You can use the same mnemonic technique to find out in which direction the vector should point to depending on the convention you are using.
    # In the case of a right-hand coordinate system, if you align the index finger along the
    # A vector (for example the tangent at a point on the surface) and the middle finger along the B vector (the bitangent if you try to figure out the orientation of a normal), the thumb will point in the direction of the C vector (the normal).

    # also - the cross product is the area for the parallelogram from the two vectors (we also need to consider the orientation)
    # if A is on the left the area will be negative and if B is on the left the area will be positive
    # the more perpendicular vectors are the larger that area will be

    # how do these two concepts work together?
    # the length of the created vector equals the area of the parallelogram
    def cross(self, v: Vector3):
        a = self
        b = v
        crossX = a.y * b.z - a.z * b.y
        crossY = a.z * b.x - a.x * b.z
        crossZ = a.x * b.y - a.y * b.x
        return Vector3(crossX, crossY, crossZ)

    def add(self, v: Vector3):
        self.x += v.x
        self.y += v.y
        self.z += v.z

    def subtract(self, v: Vector3):
        self.x -= v.x
        self.y -= v.y
        self.z -= v.z

    def multiply(self, n: float):
        self.x *= n
        self.y *= n
        self.z *= n

    def divide(self, n: float):
        self.x /= n
        self.y /= n
        self.z /= n

    def multByMatrix(self, matrix_obj: Matrix4):
        m = matrix_obj.m
        self.x = self.x * m[0][0] + self.y * \
            m[1][0] + self.z * m[2][0] + m[3][0]
        self.y = self.x * m[0][1] + self.y * \
            m[1][1] + self.z * m[2][1] + m[3][1]
        self.z = self.x * m[0][2] + self.y * \
            m[1][2] + self.z * m[2][2] + m[3][2]
        w = self.x * m[0][3] + self.y * m[1][3] + self.z * m[2][3] + m[3][3]

        # almost never this will be the case but if it is we want to normalize the point so that w is 1
        # an alternative approach would be to have two functions, one that normalizes and one that doesn't
        # that would be a more performant solution
        if w != 1 and w != 0:
            self.x = self.x / w
            self.y = self.y / w
            self.z = self.z / w
