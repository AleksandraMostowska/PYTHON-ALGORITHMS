import pytest
from am_algorithms.text.cipher import transposition_cipher


@pytest.mark.parametrize('text, expected', [
    ("lokomotywa", "olokomytaw"),
    ("abcdef", "badcfe"),
    ("123456", "214365"),
    ("", ""),
])
def test_valid_input(text, expected):
    assert transposition_cipher(text) == expected


def test_empty_input():
    with pytest.raises(ValueError, match="Text length must be even for transposition cipher"):
        transposition_cipher("a")

def test_invalid_text_length():
    with pytest.raises(ValueError, match="Text length must be even for transposition cipher"):
        transposition_cipher("lokomotywaa")