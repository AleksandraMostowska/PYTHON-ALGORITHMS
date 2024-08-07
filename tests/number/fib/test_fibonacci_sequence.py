import pytest
from am_algorithms.number.fib import (
    NthFibonacciNumberRec,
    NthFibonacciNumberFormula,
    NthFibonacciNumberIter,
    fibonacci_sequence
)

@pytest.mark.parametrize('n,expected_sequence', [
    (0, [0]),
    (1, [0, 1]),
    (2, [0, 1, 1]),
    (3, [0, 1, 1, 2]),
    (4, [0, 1, 1, 2, 3]),
    (5, [0, 1, 1, 2, 3, 5]),
    (6, [0, 1, 1, 2, 3, 5, 8]),
    (7, [0, 1, 1, 2, 3, 5, 8, 13]),
    (8, [0, 1, 1, 2, 3, 5, 8, 13, 21]),
    (9, [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]),
])
def test_valid_input_fibonacci_sequence(n, expected_sequence):
    fib_calc_iter = NthFibonacciNumberIter()
    assert fibonacci_sequence(fib_calc_iter, n) == expected_sequence
    fib_calc_rec = NthFibonacciNumberRec()
    assert fibonacci_sequence(fib_calc_rec, n) == expected_sequence
