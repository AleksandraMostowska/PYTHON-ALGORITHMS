import pytest
from am_algorithms.geometry.point import Point


@pytest.mark.parametrize('x, y, z, expected', [
    (Point(0, 0), Point(5, 5), Point(2, 2), True),
    (Point(0, 0), Point(5, 5), Point(6, 2), False),
    (Point(0, 0), Point(5, 5), Point(6, 10), False),
    (Point(0, 0), Point(5, 5), Point(5, 0), True),
    (Point(0, 0), Point(5, 5), Point(0, 5), True)
])
def test_valid_input(x, y, z, expected):
    assert z.is_on_segment(x, y) == expected

