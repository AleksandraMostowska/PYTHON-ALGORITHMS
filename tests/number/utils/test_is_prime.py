import pytest
from am_algorithms.number.utils import is_prime

@pytest.mark.parametrize('test_input,expected', [
    (2, True),
    (3, True),
    (4, False),
    (5, True),
    (25, False),
    (29, True),
    (121, False)
])
def test_valid_input_is_prime(test_input, expected):
    assert is_prime(test_input) == expected