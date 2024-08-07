import pytest
from am_algorithms.number.find_min_element import FindMinWithMax


class TestFindMinWithMax:
    @pytest.mark.parametrize("nums, expected", [
        ([0, 0, 0, 1, -1, 0], (-1, 1)),
        ([100, 200, 150, 50, 75, 25, 300], (25, 300)),
        ([3], (3, 3)),
        ([-3, 2, -2, 1, -1, 0], (-3, 2)),
        ([7, 14, 21, 28, 35], (7, 35)),
        ([5, 5, 5, 5], (5, 5)),
    ])
    def test_valid_input(self, nums, expected):
        finder = FindMinWithMax()
        assert finder.value(nums) == expected


