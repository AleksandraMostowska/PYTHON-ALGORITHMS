import pytest
from am_algorithms.number.utils import get_divisors

@pytest.mark.parametrize('test_input,expected', [
    (28, [1, 2, 4, 7, 14, 28]),
    (6, [1, 2, 3, 6]),
    (1, [1]),
    (12, [1, 2, 3, 4, 6, 12]),
    (496, [1, 2, 4, 8, 16, 31, 62, 124, 248, 496]),
    (27, [1, 3, 9, 27]),
    (100, [1, 2, 4, 5, 10, 20, 25, 50, 100]),
    (0, []),
    (-6, [])
])
def test_valid_input(test_input, expected):
    assert get_divisors(test_input) == expected