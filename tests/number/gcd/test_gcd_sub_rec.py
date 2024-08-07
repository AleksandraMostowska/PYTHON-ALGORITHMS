from am_algorithms.number.gcd import GcdSubRec


def test_valid_input_gcd_sub_rec(gcd_test_data):
    for test_input_a, test_input_b, expected in gcd_test_data:
        assert GcdSubRec().value(test_input_a, test_input_b) == expected

