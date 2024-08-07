import pytest
from am_algorithms.text.utils import naive_string_search


@pytest.mark.parametrize('pattern, text, expected', [
    ("motyw", "lokomotywa", 4),
    ("notfound", "lokomotywa", -1),
    ("mot", "motmotmot", 0),
    ("mot", "motmotmot", 0),
    ("o", "lokomotywa", 1),
    ("k", "lokomotywa", 2),
    ("w", "lokomotywa", 8),
    ("", "lokomotywa", -1),
    ("motyw", "", -1)
])
def test_naive_string_search(pattern, text, expected):
    assert naive_string_search(pattern, text) == expected

