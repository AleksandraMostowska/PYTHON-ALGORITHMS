import pytest
from am_algorithms.geometry.point import Point, Position


@pytest.mark.parametrize('p, p1, p2, expected', [
    (Point(2, 2), Point(0, 0), Point(5, 5), Position.POINT_IS_ON_THE_LINE.value),
    (Point(6, 2), Point(0, 0), Point(5, 5), Position.POINT_IS_ON_THE_RIGHT_SIDE_OF_THE_LINE.value),
    (Point(6, 10), Point(0, 0), Point(5, 5), Position.POINT_IS_ON_THE_LEFT_SIDE_OF_THE_LINE.value),
    (Point(5, 0), Point(0, 0), Point(5, 5), Position.POINT_IS_ON_THE_RIGHT_SIDE_OF_THE_LINE.value),
    (Point(0, 5), Point(0, 0), Point(5, 5), Position.POINT_IS_ON_THE_LEFT_SIDE_OF_THE_LINE.value),
    (Point(0, 2), Point(0, 0), Point(0, 5), Position.POINT_IS_ON_THE_LINE.value)
])
def test_valid_input(p, p1, p2, expected):
    assert p.position_relative_to_line(p1, p2) == expected

