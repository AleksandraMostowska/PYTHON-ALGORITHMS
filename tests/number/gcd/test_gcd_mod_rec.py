from am_algorithms.number.gcd import GcdModRec


def test_valid_input_gcd_mod_rec(gcd_test_data):
    for test_input_a, test_input_b, expected in gcd_test_data:
        assert GcdModRec().value(test_input_a, test_input_b) == expected
