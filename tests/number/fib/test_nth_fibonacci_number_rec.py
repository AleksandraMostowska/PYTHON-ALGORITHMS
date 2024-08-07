from am_algorithms.number.fib import NthFibonacciNumberRec


def test_valid_input(fib_test_data):
    for n, expected_value in fib_test_data:
        assert NthFibonacciNumberRec().value(n) == expected_value

