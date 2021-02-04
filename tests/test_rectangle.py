import sys
from pathlib import Path
import pytest

sys.path.insert(0, str(Path(__file__).parent.parent))
from rectangle_class import Rectangle
from triangle_class import Triangle
from circle_class import Circle


@pytest.mark.parametrize("length, width, result", [(5, 10, 30), (1, 5, 12)])
def test_rectangle_perimeter(length, width, result):
    r = Rectangle(length=length, width=width)
    assert r.perimeter() == result


@pytest.mark.parametrize("length, width, result", [(5, 10, 50), (1, 5, 5)])
def test_rectangle_area(length, width, result):
    r = Rectangle(length=length, width=width)
    assert r.area() == result


def test_rectangle_get_angles():
    assert Rectangle.ANGLES == 4


def test_rectangle_name():
    assert Rectangle().get_name() == "Rectangle"


@pytest.mark.parametrize("figure", [(Triangle()), (Circle())],
                         ids=["rectangle+triangle", "rectangle+circle"])
def test_rectangle_add_area(figure):
    rectangle_area = Rectangle().area()
    figure_area = figure.area()
    assert Rectangle().add_area(figure) == rectangle_area + figure_area
