import pytest
from am_algorithms.sort_generic import BubbleSort


class TestBubbleSort:

    @pytest.fixture
    def int_sorter(self):
        return BubbleSort[int]()

    @pytest.fixture
    def float_sorter(self):
        return BubbleSort[float]()

    @pytest.fixture
    def str_sorter(self):
        return BubbleSort[str]()

    def test_int_sorter(self, int_sorter, int_test_data):
        for nums, expected in int_test_data:
            assert int_sorter.sort(nums) == expected

    def test_float_sorter(self, float_sorter, float_test_data):
        for nums, expected in float_test_data:
            assert float_sorter.sort(nums) == expected

    def test_str_sorter(self, str_sorter, str_test_data):
        for nums, expected in str_test_data:
            assert str_sorter.sort(nums) == expected