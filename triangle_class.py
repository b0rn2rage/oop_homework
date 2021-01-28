from shape_class import Shapes


class Triangle(Shapes):
    def __init__(self, name="Triangle", len_first_side=5, len_second_side=7, len_third_side=9, height=4):
        super().__init__(name)
        self.len_first_side = len_first_side
        self.len_second_side = len_second_side
        self.len_third_side = len_third_side
        self.height = height
        self.angles = 3

    def perimeter(self):
        return self.len_first_side + self.len_second_side + self.len_third_side

    def area(self):
        return 0.5 * self.len_first_side * self.height

