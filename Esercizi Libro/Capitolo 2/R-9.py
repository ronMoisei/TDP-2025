"""
R-2.9 Implement the sub method for the Vector class of Section 2.3.3, so
that the expression u−v returns a new vector instance representing the
difference between two vectors.
R-2.10 Implement the neg method for the Vector class of Section 2.3.3, so
that the expression −v returns a new vector instance whose coordinates
are all the negated values of the respective coordinates of v.
R-2.12 Implement the mul method for the Vector class of Section 2.3.3, so
that the expression v 3 returns a new vector with coordinates that are 3
times the respective coordinates of v.
R-2.13 Exercise R-2.12 asks for an implementation of mul , for the Vector
class of Section 2.3.3, to provide support for the syntax v 3. Implement
the rmul method, to provide additional support for syntax 3 v.
R-2.14 Implement the mul method for the Vector class of Section 2.3.3, so
that the expression u v returns a scalar that represents the dot product of
the vectors, that is, Σd_i = u_i · v_i.

R-2.11 In Section 2.3.3, we note that our Vector class supports a syntax such as
v = u + [5, 3, 10, −2, 1], in which the sum of a vector and list returns
a new vector. However, the syntax v = [5, 3, 10, −2, 1] + u is illegal.
Explain how the Vector class definition can be revised so that this syntax
generates a new vector.
"""





from math import sqrt
from typing import Sequence

class Vector:
    def __init__(self, x: float, y: float, z: float):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"

    def __len__(self):
        return len(self.x)

    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x + other.x,
                          self.y + other.y,
                          self.z + other.z)
        elif isinstance(other, Sequence) and len(other) == 3:
            return Vector(self.x + other[0],
                          self.y + other[1],
                          self.z + other[2])
        else:
            raise TypeError("Must be a Vector")
    def __sub__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y, self.z - other.z)
        else:
            raise TypeError("Vector must be of type Vector")

    def __mul__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x * other.x, self.y * other.y, self.z * other.z)
        elif isinstance(other, int):
            return Vector(self.x * other, self.y * other, self.z * other)
        else:
            raise TypeError("Must be a Vector or scalar")

    def __eq__(self, other):
        if isinstance(other, Vector):
            return self.x == other.x and self.y == other.y and self.z == other.z

    def printmul(self, other):
        if isinstance(other, Vector):
            print(f"il vettore è lungo {round(Vector(self.x * other.x, self.y * other.y, self.z * other.z).module())}:\n{round(Vector(self.x * other.x, self.y * other.y, self.z * other.z).module()) * "."}")

    def module(self):
        return sqrt(self.x**2 + self.y**2 + self.z**2)

if __name__ == "__main__":
    v1 = Vector(1, 2, 3)
    v2 = Vector(4, 5, 6)

    v1.printmul(v2)

    s = v1 + v2
    print(s)

    print(v1 + [2, 2, 2])
    v3 = [1,1,1] + v1