import sys
from pathlib import Path
import pytest

sys.path.insert(0, str(Path(__file__).parent.parent))
from square_class import Square
from triangle_class import Triangle
from circle_class import Circle


@pytest.mark.parametrize("side_length, result", [(5, 20), (20, 80)])
def test_square_perimeter(side_length, result):
    s = Square(side_length=side_length)
    assert s.perimeter() == result


@pytest.mark.parametrize("side_length, result", [(5, 25), (20, 400)])
def test_square_area(side_length, result):
    r = Square(side_length=side_length)
    assert r.area() == result


def test_square_get_angles():
    assert Square.ANGLES == 4


def test_square_name():
    assert Square().get_name() == "Square"


@pytest.mark.parametrize("figure", [(Triangle()), (Circle())],
                         ids=["square+triangle", "square+circle"])
def test_square_add_area(figure):
    square_area = Square().area()
    figure_area = figure.area()
    assert Square().add_area(figure) == square_area + figure_area
