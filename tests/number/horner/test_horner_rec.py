import pytest
from am_algorithms.number.horner import HornerRec


@pytest.fixture
def horner_rec_instance():
    return HornerRec()


@pytest.mark.parametrize('poly, n, x, expected', [
    ([3, 2, 1], 2, 2, 17),
    ([1, 0, 3], 2, 3, 12),
    ([5, -4, 3, -2, 1], 4, -1, 15),
    ([1], 0, 5, 1),
    ([-1, 4, -5, 6], 3, 1, 4)
])
def test_horner_rec_valid(horner_rec_instance: HornerRec, poly: list[int], n: int, x: int, expected: int) -> None:
    assert horner_rec_instance.value(poly, n, x) == expected


def test_with_negative_degree_n(horner_rec_instance: HornerRec) -> None:
    with pytest.raises(ValueError, match="Degree cannot be negative number"):
        horner_rec_instance.value([1, 2, 3], -1, 5)


def test_with_invalid_degree_and_poly_len(horner_rec_instance: HornerRec) -> None:
    with pytest.raises(ValueError, match="Degree and values of polynomial do not match"):
        horner_rec_instance.value([1, 2], 3, 1)