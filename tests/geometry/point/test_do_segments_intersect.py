import pytest
from am_algorithms.geometry.point import Point, do_segments_intersect


@pytest.mark.parametrize('p1, q1, p2, q2, expected', [
    (Point(1, 1), Point(10, 1), Point(1, 2), Point(10, 2), False),
    (Point(10, 0), Point(0, 10), Point(0, 0), Point(10, 10), True),
    (Point(-5, -5), Point(0, 0), Point(1, 1), Point(10, 10), False)
])
def test_valid_input(p1, q1, p2, q2, expected):
    assert do_segments_intersect(p1, q1, p2, q2) == expected

