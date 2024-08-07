import pytest
from am_algorithms.number.numerical_integration import IntegrationRectangleMethod


def example_function(x):
    return x * x + x + 2


@pytest.fixture
def integration_method():
    return IntegrationRectangleMethod()


@pytest.mark.parametrize('a, b, n, expected', [
    (0, 1, 100, 2.83335),
    (-1, 1, 100, 4.6668),
    (0, 1, 50, 2.8334),
    (0, 1, 10, 2.835),
])
def test_valid_input(integration_method, a, b, n, expected):
    result = integration_method.integrate(example_function, a, b, n)
    assert result
    assert abs(result - expected) < 0.4


def test_when_a_greater_than_or_equal_to_b(integration_method):
    with pytest.raises(ValueError, match="Lower limit 'a' must be less than upper limit 'b'"):
        integration_method.integrate(example_function, 1, 1, 100)


def test_when_n_is_non_positive(integration_method):
    with pytest.raises(ValueError, match="Number of subintervals 'n' must be positive"):
        integration_method.integrate(example_function, 0, 1, 0)
