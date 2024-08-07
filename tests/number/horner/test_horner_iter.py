import pytest
from am_algorithms.number.horner import HornerIter


@pytest.fixture
def horner_iter_instance():
    return HornerIter()


@pytest.mark.parametrize('poly, n, x, expected', [
    ([3, 2, 1], 2, 2, 17),
    ([1, 0, 3], 2, 3, 12),
    ([5, 4], 1, 2, 14),
    ([1], 0, 5, 1),
])
def test_horner_iter_valid(horner_iter_instance: HornerIter, poly: list[int], n: int, x: int, expected: int) -> None:
    assert horner_iter_instance.value(poly, n, x) == expected


def test_horner_iter_with_negative_degree_n(horner_iter_instance: HornerIter) -> None:
    with pytest.raises(ValueError, match="Degree cannot be negative number"):
        horner_iter_instance.value([1, 2, 3], -1, 5)


def test_horner_iter_with_invalid_degree_and_poly_len(horner_iter_instance: HornerIter) -> None:
    with pytest.raises(ValueError, match="Degree and values of polynomial do not match"):
        horner_iter_instance.value([1, 2], 3, 1)
