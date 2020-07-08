class Vector:
    """Represent a vector in a multidimensional space"""

    def __init__(self, d):
        """create d-dimensional vector of zeros"""
        self._coords = [0] * d

    def __len__(self):
        """Return the dimension of the vector"""
        return len(self._coords)

    def __getitem__(self, j):
        """Return jth coordinate of the vector"""
        return self._coords[j]

    def __setitem__(self, j, value):
        """set jth coordinate of the vector to given value"""
        self._coords[j] = value

    def __add__(self, other):
        """Return the sum of two vectors"""
        if len(self) != len(other):
            raise ValueError('dimensions must agree')
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] + other[j]
        return result

    def __eq__(self, other):
        """Return True if both vectors have the same coordinates as the other vector"""
        return self._coords == other._coords

    def __ne__(self, other):
        return not (self == other)

    def __str__(self):
        """Produce the string representation of vector"""
        return f'< {str(self._coords)[1:-1]} >'
