from shape_class import Shapes
from math import pi


class Circle(Shapes):
    def __init__(self, name="Circle", radius=3):
        super().__init__(name)
        self.radius = radius
        self.angles = 0

    def perimeter(self):
        return 2 * pi * self.radius

    def area(self):
        return pi * self.radius ** 2

