import pytest
from am_algorithms.text.utils import is_palindrome


@pytest.mark.parametrize('input,expected', [
    ("racecar", True),
    ("hello", False),
    ("", True),
    ("a", True),
    ("A man a plan a canal Panama".replace(" ", "").lower(), True),
    ("No lemon, no melon".replace(" ", "").replace(",", "").lower(), True),
    ("Was it a car or a cat I saw".replace(" ", "").lower(), True),
    ("12321", True),
    ("12345", False)
])
def test_valid_input(input, expected):
    assert is_palindrome(input) == expected
