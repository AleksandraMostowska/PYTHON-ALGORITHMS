import pytest
from am_algorithms.number.utils import convert_to_base


@pytest.mark.parametrize('n, base, expected', [
    (255, 16, "FF"),
    (10, 2, "1010"),
    (1234, 10, "1234"),
    (1234, 16, "4D2"),
    (0, 10, "0"),
    (0, 16, "0"),
    (1, 16, "1"),
    (16, 16, "10"),
    (255, 8, "377"),
    (255, 3, "100110")
])
def test_valid_input(n, base, expected):
    assert convert_to_base(n, base) == expected

