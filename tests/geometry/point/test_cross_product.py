import pytest
from am_algorithms.geometry.point import Point


@pytest.mark.parametrize('p1, p2, p3, expected', [
    (Point(1, 1), Point(2, 2), Point(3, 3), 0),
    (Point(1, 1), Point(2, 2), Point(4, 5), 2),
    (Point(1, 1), Point(2, 2), Point(4, 3), 1)
])
def test_valid_input(p1, p2, p3, expected):
    assert p1.cross_product(p2, p3) == expected
