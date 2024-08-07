import pytest
from am_algorithms.geometry.triangle import Triangle, TriangleType
from am_algorithms.geometry.point import Point


@pytest.mark.parametrize('points, expected_type', [
    (Triangle(Point(0, 0), Point(2, 0), Point(1, 1.73205)), TriangleType.EQUILATERAL),
    (Triangle(Point(1, 1), Point(-1, 1), Point(0, 2.73205)), TriangleType.EQUILATERAL),
])
def test_equilateral_triangle(points, expected_type):
    assert points.get_triangle_type() == expected_type


@pytest.mark.parametrize('points, expected_type', [
    (Triangle(Point(-1, -1), Point(1, -1), Point(0, 2)), TriangleType.ISOSCELES),
    (Triangle(Point(0, 0), Point(4, 0), Point(2, 2)), TriangleType.ISOSCELES),
])
def test_isosceles_triangle(points, expected_type):
    assert points.get_triangle_type() == expected_type


@pytest.mark.parametrize('points, expected_type', [
    (Triangle(Point(0, 0), Point(3, 0), Point(0, 4)), TriangleType.RIGHT_ANGLED),
    (Triangle(Point(1, 1), Point(4, 1), Point(1, 5)), TriangleType.RIGHT_ANGLED),
])
def test_right_angled_triangle(points, expected_type):
    assert points.get_triangle_type() == expected_type


@pytest.mark.parametrize('points, expected_type', [
    (Triangle(Point(2, 1), Point(5, 1), Point(3, 4)), TriangleType.ACUTE),
    (Triangle(Point(0, 0), Point(3, 0), Point(1, 2)), TriangleType.ACUTE),
])
def test_acute_triangle(points, expected_type):
    assert points.get_triangle_type() == expected_type


@pytest.mark.parametrize('points, expected_type', [
    (Triangle(Point(0, 0), Point(8, 0), Point(10, 3)), TriangleType.OBTUSE),
    (Triangle(Point(0, 0), Point(5, -3), Point(6, -2)), TriangleType.OBTUSE),
])
def test_obtuse_triangle(points, expected_type):
    assert points.get_triangle_type() == expected_type


@pytest.mark.parametrize('points, expected_type', [
    (Triangle(Point(0, 0), Point(1, 1), Point(2, 2)), None),
    (Triangle(Point(0, 0), Point(0, 1), Point(0, 2)), None)
])
def test_non_triangle(points, expected_type):
    assert points.get_triangle_type() == expected_type
