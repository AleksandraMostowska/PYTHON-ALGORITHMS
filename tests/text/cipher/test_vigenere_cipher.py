import pytest
from am_algorithms.text.cipher import vigenere_cipher


@pytest.mark.parametrize('text, key, expected', [
    ("abc", "key", "kfa"),
    ("xyz", "cipher", "zgo"),
    ("ABC", "VIGENERE", "VJI"),
    ("Hello, World!", "SECRET", "Zincs, Pgvnu!"),
    ("abcdefghijklmnopqrstuvwxyz", "python", "pzvkssvfbqyyblhweehrnckknx"),
    ("ABCDEFGHIJKLMNOPQRSTUVWXYZ", "Python", "PZVKSSVFBQYYBLHWEEHRNCKKNX"),
    ("", "key", ""),
    ("123abc", "key", "123kfa")
])
def test_valid_input(text, key, expected):
    assert vigenere_cipher(text, key) == expected