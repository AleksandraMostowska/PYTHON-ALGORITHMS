import pytest
from math import isclose
from am_algorithms.geometry.point import Point


@pytest.mark.parametrize('p1, p2, expected_distance', [
    (Point(0, 0), Point(5, 5), 5 * (2 ** 0.5)),
    (Point(1, 1), Point(4, 5), 5),
    (Point(-1, -1), Point(2, 2), 3 * (2 ** 0.5)),
    (Point(0, 0), Point(0, 0), 0),
    (Point(0, 0), Point(3, 4), 5)
])
def test_distance_to(p1, p2, expected_distance):
    assert isclose(p1.distance_to(p2), expected_distance, rel_tol=1e-9)
