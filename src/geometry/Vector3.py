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

    def dot(self):
        pass

    def cross(self):
        pass
