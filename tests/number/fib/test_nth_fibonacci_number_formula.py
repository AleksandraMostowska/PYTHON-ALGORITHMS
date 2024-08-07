from am_algorithms.number.fib import NthFibonacciNumberFormula


def test_valid_input(fib_test_data):
    for n, expected_value in fib_test_data:
        assert NthFibonacciNumberFormula().value(n) == expected_value
