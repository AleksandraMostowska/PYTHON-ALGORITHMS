import pytest
from am_algorithms.number.bisection import BisectionRec


def example_function(x):
    return x * (x * (x - 3) + 2) - 6


@pytest.fixture
def bisection_rec_method() -> BisectionRec:
    return BisectionRec()


@pytest.mark.parametrize('a, b, epsilon, expected', [
    (-10, 10, 0.0001, 3.0)
])
def test_bisection_rec_method_valid(bisection_rec_method, a, b, epsilon, expected):
    result = bisection_rec_method.bisection_method(example_function, a, b, epsilon)
    assert abs(result - expected) < epsilon


def test_when_a_greater_than_or_equal_to_b(bisection_rec_method: BisectionRec) -> None:
    with pytest.raises(ValueError, match="Lower limit 'a' must be less than upper limit 'b'"):
        bisection_rec_method.bisection_method(example_function, 2.0, 1.0, 1e-6)


def test_when_epsilon_is_non_positive(bisection_rec_method: BisectionRec) -> None:
    with pytest.raises(ValueError, match="Tolerance 'epsilon' must be positive"):
        bisection_rec_method.bisection_method(example_function, 1.0, 2.0, 0.0)
