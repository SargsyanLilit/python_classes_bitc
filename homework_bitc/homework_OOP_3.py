class Triangle(object):
    instance_number = 0

    def __new__(cls, *args, **kwargs):
        cls.instance_number += 1
        return super().__new__(cls)

    def __init__(self, side_1, side_2, side_3):
        self.side_1 = side_1
        self.side_2 = side_2
        self.side_3 = side_3

    def __eq__(self, other):
        if not isinstance(other, Triangle):
            raise ValueError("Wrong Input")
        sorted_triangle_sides = sorted([self.side_1, self.side_2, self.side_3])
        sorted_other_sides = sorted([other.side_1, other.side_2, other.side_3])
        return sorted_triangle_sides[0] == sorted_other_sides[0] and \
               sorted_triangle_sides[1] == sorted_other_sides[1] and \
               sorted_triangle_sides[2] == sorted_other_sides[2]

    def area(self):
        s = (self.side_1 + self.side_2 + self.side_3)/2
        return (s * (s - self.side_1) * (s - self.side_2) * (s - self.side_3)) ** 0.5

    def perimeter(self):
        return self.side_1 + self.side_2 + self.side_3

    def is_alike(self, other):
        if not isinstance(other, Triangle):
            raise ValueError("Wrong Input")
        sorted_triangle_sides = sorted([self.side_1, self.side_2, self.side_3])
        sorted_other_sides = sorted([other.side_1, other.side_2, other.side_3])
        return sorted_triangle_sides[0]/sorted_other_sides[0] == \
               sorted_triangle_sides[1]/sorted_other_sides[1] == \
               sorted_triangle_sides[2]/sorted_other_sides[2]


class Rectangular(object):

    def __init__(self, side_1, side_2, side_3):
        self.side_1 = side_1
        self.side_2 = side_2
        self.side_3 = side_3

    def __eq__(self, other):
        if not isinstance(other, Rectangular):
            raise ValueError("Wrong Input")
        sorted_rectangular_sides = sorted([self.side_1, self.side_2, self.side_3])
        sorted_other_sides = sorted([other.side_1, other.side_2, other.side_3])
        return sorted_rectangular_sides[0] == sorted_other_sides[0] and \
               sorted_rectangular_sides[1] == sorted_other_sides[1] and \
               sorted_rectangular_sides[2] == sorted_other_sides[2]

    def __lt__(self, other):
        if not isinstance(other, Rectangular):
            raise ValueError("Wrong Input")
        sorted_rectangular_sides = sorted([self.side_1, self.side_2, self.side_3])
        sorted_other_sides = sorted([other.side_1, other.side_2, other.side_3])
        return sorted_rectangular_sides[0] < sorted_other_sides[0] and \
               sorted_rectangular_sides[1] < sorted_other_sides[1] and \
               sorted_rectangular_sides[2] < sorted_other_sides[2]


class Cube(Rectangular):

    def __init__(self, side):
        Rectangular.__init__(self, side, side, side)