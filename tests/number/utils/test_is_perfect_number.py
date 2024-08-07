import pytest
from am_algorithms.number.utils import is_perfect_number

@pytest.mark.parametrize('test_input,expected', [
    (6, True),
    (28, True),
    (496, True),
    (8128, True),
    (12, False),
    (27, False)
])
def test_is_perfect_number_with_valid_input(test_input, expected):
    assert is_perfect_number(test_input) == expected
