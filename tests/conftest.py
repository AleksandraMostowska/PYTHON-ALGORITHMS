import pytest

@pytest.fixture
def int_test_data():
    return [
        ([4, 2, 7, 1, 3], [1, 2, 3, 4, 7]),
        ([10, 9, 8, 7, 6, 5], [5, 6, 7, 8, 9, 10]),
        ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
        ([5, 1, 4, 2, 8], [1, 2, 4, 5, 8]),
        ([], []),
        ([3], [3]),
    ]

@pytest.fixture
def float_test_data():
    return [
        ([4.5, 2.2, 7.1, 1.0, 3.3], [1.0, 2.2, 3.3, 4.5, 7.1]),
        ([10.1, 9.9, 8.8, 7.7, 6.6, 5.5], [5.5, 6.6, 7.7, 8.8, 9.9, 10.1]),
        ([1.1, 2.2, 3.3, 4.4, 5.5], [1.1, 2.2, 3.3, 4.4, 5.5]),
        ([5.5, 1.1, 4.4, 2.2, 8.8], [1.1, 2.2, 4.4, 5.5, 8.8]),
        ([], []),
        ([3.3], [3.3]),
    ]

@pytest.fixture
def str_test_data():
    return [
        (["pear", "apple", "banana", "orange"], ["apple", "banana", "orange", "pear"]),
        (["zebra", "ant", "elephant", "dog"], ["ant", "dog", "elephant", "zebra"]),
        (["a", "b", "c"], ["a", "b", "c"]),
        ([], []),
        (["apple"], ["apple"]),
    ]


@pytest.fixture
def gcd_test_data():
    return [
        (48, 18, 6),
        (0, 18, 18),
        (48, 0, 48),
        (-48, 18, 6),
        (48, -18, 6)
    ]


@pytest.fixture
def fib_test_data():
    return [
        (0, 0),
        (1, 1),
        (2, 1),
        (3, 2),
        (12, 144),
        (13, 233),
        (14, 377),
        (15, 610),
        (16, 987)
    ]