import pytest
from am_algorithms.geometry.point import Point


@pytest.mark.parametrize('p, segment_start, segment_end, expected', [
    (Point(2, 2), Point(0, 0), Point(5, 5), True),
    (Point(6, 2), Point(0, 0), Point(5, 5), False),
    (Point(6, 10), Point(0, 0), Point(5, 5), False),
    (Point(5, 0), Point(0, 0), Point(5, 5), False),
    (Point(0, 5), Point(0, 0), Point(5, 5), False),
    (Point(0, 2), Point(0, 0), Point(0, 5), True)
])
def test_valid_input(p, segment_start, segment_end, expected):
    assert p.point_on_segment(segment_start, segment_end) == expected
