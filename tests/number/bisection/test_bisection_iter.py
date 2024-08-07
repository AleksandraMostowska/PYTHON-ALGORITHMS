import pytest
from am_algorithms.number.bisection import BisectionIter


def example_function(x):
    return x * (x * (x - 3) + 2) - 6


@pytest.fixture
def bisection_iter_method() -> BisectionIter:
    return BisectionIter()


@pytest.mark.parametrize('a, b, epsilon, expected', [
    (-10, 10, 0.00001, 3.0)
])
def test_bisection_iter_method_valid(bisection_iter_method, a, b, epsilon, expected):
    result = bisection_iter_method.bisection_method(example_function, a, b, epsilon)
    assert abs(result - expected) < epsilon


def test_when_a_greater_than_or_equal_to_b(bisection_iter_method: BisectionIter) -> None:
    with pytest.raises(ValueError, match="Lower limit 'a' must be less than upper limit 'b'"):
        bisection_iter_method.bisection_method(example_function, 2.0, 1.0, 1e-6)


def test_when_epsilon_is_non_positive(bisection_iter_method: BisectionIter) -> None:
    with pytest.raises(ValueError, match="Tolerance 'epsilon' must be positive"):
        bisection_iter_method.bisection_method(example_function, 1.0, 2.0, 0.0)
