import pytest
from am_algorithms.text.cipher import caesar_cipher


@pytest.mark.parametrize('text, key, expected', [
    ("abc", 3, "def"),
    ("xyz", 3, "abc"),
    ("ABC", 3, "DEF"),
    ("XYZ", 3, "ABC"),
    ("Hello, World!", 5, "Mjqqt, Btwqi!"),
    ("abcdefghijklmnopqrstuvwxyz", 1, "bcdefghijklmnopqrstuvwxyza"),
    ("ABCDEFGHIJKLMNOPQRSTUVWXYZ", 1, "BCDEFGHIJKLMNOPQRSTUVWXYZA"),
    ("", 0, ""),
    ("", 5, "")
])
def test_valid_input(text, key, expected):
    assert caesar_cipher(text, key) == expected


def test_out_of_range_key():
    with pytest.raises(ValueError, match="Key must be in the range between 0 and 25"):
        caesar_cipher("abc", 26)
