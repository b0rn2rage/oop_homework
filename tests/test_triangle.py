import sys
from pathlib import Path
import pytest

sys.path.insert(0, str(Path(__file__).parent.parent))
from triangle_class import Triangle
from rectangle_class import Rectangle
from square_class import Square


@pytest.mark.parametrize("len_first, len_second, len_third, result", [(5, 10, 15, 30), (1, 2, 3, 6)])
def test_triangle_perimeter(len_first, len_second, len_third, result):
    t = Triangle(len_first_side=len_first, len_second_side=len_second, len_third_side=len_third)
    assert t.perimeter() == result


@pytest.mark.parametrize("len_first, height, result", [(5, 10, 25), (3, 3, 4.5)])
def test_triangle_area(len_first, height, result):
    t = Triangle(len_first_side=len_first, height=height)
    assert t.area() == result


def test_triangle_get_angles():
    assert Triangle.ANGLES == 3


def test_triangle_name():
    assert Triangle().get_name() == "Triangle"


@pytest.mark.parametrize("figure", [(Rectangle()), (Square())],
                         ids=["triangle+rectangle", "triangle+square"])
def test_triangle_add_area(figure):
    triangle_area = Triangle().area()
    figure_area = figure.area()
    assert Triangle().add_area(figure) == triangle_area + figure_area
