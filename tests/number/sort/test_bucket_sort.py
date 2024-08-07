import pytest
from am_algorithms.number.sort import BucketSort


class TestBucketSort:

    @pytest.fixture
    def sorter(self):
        return BucketSort()

    def test_valid_input(self, sorter, int_test_data):
        for nums, expected in int_test_data:
            assert sorter.sort(nums) == expected
