from shape_class import Shapes


class Square(Shapes):
    ANGLES = 4

    def __init__(self, name="Square", side_length=5):
        super().__init__(name)
        self.side_length = side_length

    def perimeter(self):
        return 4 * self.side_length

    def area(self):
        return self.side_length ** 2


