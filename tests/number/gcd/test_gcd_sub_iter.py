from am_algorithms.number.gcd import GcdSubIter


def test_valid_input(gcd_test_data):
    for test_input_a, test_input_b, expected in gcd_test_data:
        assert GcdSubIter().value(test_input_a, test_input_b) == expected
