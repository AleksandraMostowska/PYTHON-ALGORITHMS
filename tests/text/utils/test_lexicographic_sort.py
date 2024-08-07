import pytest
from am_algorithms.text.utils import lexicographic_sort


@pytest.mark.parametrize('test_input,expected', [
    (["banana", "apple", "cherry"], ["apple", "banana", "cherry"]),
    (["abc", "ab", "abcd"], ["ab", "abc", "abcd"]),
    (["zebra", "apple", "orange"], ["apple", "orange", "zebra"]),
    (["a", "b", "a"], ["a", "a", "b"]),
    ([""], [""]),
    ([], []),
    (['apple', 'Apple'], ['Apple', 'apple'])
])
def test_lexicographic_sort(test_input, expected):
    assert lexicographic_sort(test_input) == expected


