import pytest
from math import isclose
from am_algorithms.geometry.point import Point
from am_algorithms.geometry.triangle import Triangle


@pytest.mark.parametrize('triangle, expected_sides', [
    (Triangle(Point(0, 0), Point(5, 0), Point(0, 5)), (5.0, 7.0710678118654755, 5.0)),
    (Triangle(Point(1, 1), Point(4, 1), Point(1, 5)), (3.0, 5.0, 4.0)),
    (Triangle(Point(-1, -1), Point(2, -1), Point(-1, 2)), (3.0, 4.242640687119285, 3.0)),
    (Triangle(Point(0, 0), Point(0, 1), Point(1, 0)), (1.0, 1.4142135623730951, 1.0)),
    (Triangle(Point(0, 0), Point(1, 1), Point(1, 0)), (1.4142135623730951, 1.0, 1.0))
])
def test_get_sides_of_triangle(triangle, expected_sides):
    sides = triangle.get_sides_of_triangle()
    assert all(isclose(side, expected_side, rel_tol=1e-9) for side, expected_side in zip(sides, expected_sides))
