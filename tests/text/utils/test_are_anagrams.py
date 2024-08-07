import pytest
from am_algorithms.text.utils import are_anagrams

@pytest.mark.parametrize('t1, t2, expected', [
    ('listen', 'silent', True),
    ('triangle', 'integral', True),
    ('apple', 'pale', False),
    ('abcd', 'dcba', True),
    ('', '', True),
    ('a', 'a', True),
    ('a', 'b', False)
])
def test_valid_input(t1, t2, expected):
    assert are_anagrams(t1, t2) == expected


def test_different_lengths():
    assert not are_anagrams('abcd', 'abcde')