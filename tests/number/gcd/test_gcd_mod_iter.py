from am_algorithms.number.gcd import GcdModIter


def test_valid_input_gcd_mod_iter(gcd_test_data):
    for test_input_a, test_input_b, expected in gcd_test_data:
        assert GcdModIter().value(test_input_a, test_input_b) == expected

