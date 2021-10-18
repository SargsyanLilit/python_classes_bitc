class ThreeSidedShape(object):

    def __init__(self, side_1, side_2, side_3):
        self.side_1 = side_1
        self.side_2 = side_2
        self.side_3 = side_3

    @staticmethod
    def to_sorted_list(obj):
        return sorted([obj.side_1, obj.side_2, obj.side_3])

    def instance_checker(self, obj):
        if not isinstance(obj, type(self)):
            raise ValueError("Wrong Input")

    def __eq__(self, other):
        ThreeSidedShape.instance_checker(self, other)
        return ThreeSidedShape.to_sorted_list(self) == ThreeSidedShape.to_sorted_list(other)


class Triangle(ThreeSidedShape):
    instance_number = 0

    def __new__(cls, *args, **kwargs):
        cls.instance_number += 1
        return super().__new__(cls)

    def area(self):
        s = (self.side_1 + self.side_2 + self.side_3)/2
        return (s * (s - self.side_1) * (s - self.side_2) * (s - self.side_3)) ** 0.5

    def perimeter(self):
        return self.side_1 + self.side_2 + self.side_3

    def is_alike(self, other):
        ThreeSidedShape.instance_checker(self, other)
        sorted_triangle_sides = ThreeSidedShape.to_sorted_list(self)
        sorted_other_sides = ThreeSidedShape.to_sorted_list(other)
        return sorted_triangle_sides[0]/sorted_other_sides[0] == \
               sorted_triangle_sides[1]/sorted_other_sides[1] == \
               sorted_triangle_sides[2]/sorted_other_sides[2]


class Rectangular(ThreeSidedShape):

    def __lt__(self, other):
        ThreeSidedShape.instance_checker(self, other)
        sorted_rectangular_sides = ThreeSidedShape.to_sorted_list(self)
        sorted_other_sides = ThreeSidedShape.to_sorted_list(other)
        return sorted_rectangular_sides[0] < sorted_other_sides[0] and \
               sorted_rectangular_sides[1] < sorted_other_sides[1] and \
               sorted_rectangular_sides[2] < sorted_other_sides[2]


class Cube(Rectangular):

    def __init__(self, side):
        Rectangular.__init__(self, side, side, side)

