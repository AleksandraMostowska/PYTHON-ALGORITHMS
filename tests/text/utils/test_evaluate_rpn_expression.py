import pytest
from am_algorithms.text.utils import evaluate_rpn_expression


@pytest.mark.parametrize('expression, expected', [
    ("3 4 +", 7),
    ("3 4 -", -1),
    ("3 4 *", 12),
    ("6 2 /", 3),
    ("8 2 /", 4),
    ("3 4 + 5 *", 35),
    ("3 4 + 5 -", 2),
    ("3 4 5 + *", 27),
    ("", None)
])
def test_valid_input(expression, expected):
    assert evaluate_rpn_expression(expression) == expected


def test_division_by_zero():
    with pytest.raises(ZeroDivisionError, match="Division by zero error"):
        evaluate_rpn_expression("5 0 /")


def test_invalid_characters():
    with pytest.raises(ValueError, match="Invalid characters found in the expression"):
        evaluate_rpn_expression("3 $ +")
