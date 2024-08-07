import pytest
from am_algorithms.number.utils import get_square_root


@pytest.mark.parametrize('test_input, expected', [
    (25.0, 5.0),
    (16.0, 4.0),
    (9.0, 3.0),
    (2.0, 1.414213),
    (1.0, 1.0),
    (0.25, 0.5),
    (0.01, 0.1),
    (1e-6, 0.001),
    (1e6, 1000.0),
    (1e12, 1e6),
    (0, 0.0),
    (-6, 0.0)
])
def test_valid_input(test_input, expected):
    assert pytest.approx(get_square_root(test_input), rel=1e-6) == expected


@pytest.mark.parametrize('test_input, eps, expected', [
    (25.0, 1e-9, 5.0),
    (2.0, 1e-12, 1.414213562373),
])
def test_custom_eps(test_input, eps, expected):
    assert pytest.approx(get_square_root(test_input, eps), rel=eps) == expected

