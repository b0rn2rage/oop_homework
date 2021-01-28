from abc import ABC, abstractmethod


class Shapes(ABC):
    @abstractmethod
    def __init__(self, name):
        self.name = name
        self.figure = None
        self.angles = None

    @abstractmethod
    def perimeter(self):
        raise NotImplemented

    @abstractmethod
    def area(self):
        raise NotImplemented

    def add_area(self, figure):
        if isinstance(figure, Shapes):
            sum_area = self.area() + figure.area()
            return sum_area
        else:
            return "В качестве аргумента figure был передан неправильный класс"
