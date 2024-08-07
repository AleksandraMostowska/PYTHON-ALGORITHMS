import pytest
from am_algorithms.number.find_min_element import FindMinElementBySwapping


class TestFindMinElementBySwapping:
    @pytest.mark.parametrize("nums, expected", [
        ([3, 1, 4, 1, 5, 9, 2, 6, 5], 1),
        ([10, 20, 30, 40, 50], 10),
        ([1], 1),
        ([2, -1, 0, -3, 5, -6], -6),
        ([0, 0, 0, 0, 0], 0),
    ])
    def test_valid_input(self, nums, expected):
        finder = FindMinElementBySwapping()
        assert finder.value(nums) == expected