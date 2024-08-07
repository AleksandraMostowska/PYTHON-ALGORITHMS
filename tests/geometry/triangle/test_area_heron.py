import pytest
from pytest import approx
from am_algorithms.geometry.point import Point
from am_algorithms.geometry.triangle import Triangle


@pytest.mark.parametrize('x, y, z, expected', [
    (Point(0, 0), Point(3, 0), Point(0, 4), 6.0),
    (Point(0, 0), Point(3, 0), Point(3, 4), 6.0),
    (Point(0, 0), Point(5, 0), Point(0, 12), 30.0),
    (Point(1, 1), Point(1, 2), Point(2, 1), 0.5),
    (Point(0, 0), Point(1, 1), Point(2, 2), -1.0),
    (Point(0, 0), Point(1, 1), Point(2, 3), 0.5),
    (Point(0, 0), Point(1, 1), Point(2, 2), -1.0),
])
def test_area_heron(x, y, z, expected):
    assert Triangle(x, y, z).area_heron() == approx(expected, rel=1e-9)
