from shape_class import Shapes
from math import pi


class Circle(Shapes):
    ANGLES = 0

    def __init__(self, name="Circle", radius=3):
        super().__init__(name)
        self.radius = radius

    def perimeter(self):
        return 2 * pi * self.radius

    def area(self):
        return pi * self.radius ** 2
