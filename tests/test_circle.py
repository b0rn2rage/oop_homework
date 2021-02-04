import sys
from pathlib import Path
import pytest

sys.path.insert(0, str(Path(__file__).parent.parent))
from circle_class import Circle
from rectangle_class import Rectangle
from square_class import Square


@pytest.mark.parametrize("radius, result", [(5, 31.42), (1, 6.28)])
def test_circle_perimeter(radius, result):
    c = Circle(radius=radius)
    assert round(c.perimeter(), 2) == result


@pytest.mark.parametrize("radius, result", [(5, 78.54), (3, 28.27)])
def test_circle_area(radius, result):
    c = Circle(radius=radius)
    assert round(c.area(), 2) == result


def test_circle_get_angles():
    assert Circle.ANGLES == 0


def test_circle_name():
    assert Circle().get_name() == "Circle"


@pytest.mark.parametrize("figure", [(Rectangle()), (Square())],
                         ids=["circle+rectangle", "circle+square"])
def test_circle_add_area(figure):
    circle_area = Circle().area()
    figure_area = figure.area()
    assert Circle().add_area(figure) == circle_area + figure_area
