import pytest
from am_algorithms.number.utils import get_prime_factors

@pytest.mark.parametrize('test_input,expected', [
    (24, [2, 2, 2, 3]),
    (6, [2, 3]),
    (1, []),
    (12, [2, 2, 3]),
    (496, [2, 2, 2, 2, 31]),
    (27, [3, 3, 3]),
    (100, [2, 2, 5, 5]),
    (1520, [2, 2, 2, 2, 5, 19]),
    (0, []),
    (-6, []),
    (1, [])
])
def test_valid_input(test_input, expected):
    assert get_prime_factors(test_input) == expected