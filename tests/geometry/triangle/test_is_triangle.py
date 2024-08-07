import pytest
from am_algorithms.geometry.triangle import Triangle


@pytest.mark.parametrize('a, b, c, expected', [
    (3, 4, 5, True),
    (1, 1, 3, False),
    (5, 5, 5, True),
    (7, 10, 5, True),
    (1, 2, 3, False),
    (1, -2, 3, False),
    (1, 2, -3, False),
])
def test_valid_input(a, b, c, expected):
    assert Triangle.is_triangle(a, b, c) == expected

