from shape_class import Shapes


class Rectangle(Shapes):
    ANGLES = 4

    def __init__(self, name="Rectangle", length=10, width=5):
        super().__init__(name)
        self.length = length
        self.width = width

    def perimeter(self):
        return (self.length + self.width) * 2

    def area(self):
        return self.length * self.width
