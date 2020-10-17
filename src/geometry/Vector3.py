from __future__ import annotations
import math


class Vector3:

    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def length(self):
        return math.sqrt(self.x * self.x + self.y * self.y + self.z * self.z)

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
    def dot(self, v: Vector3):
        return self.x * v.x + self.y * v.y + self.z * v.z

    def cross(self):
        pass
