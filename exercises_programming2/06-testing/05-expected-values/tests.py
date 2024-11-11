import pytest
from mergesort import *

@pytest.mark.parametrize('list', [
    list(range(k)) for k in range(101)
])

def test_split_in_two(list):
    left, right = split_in_two(list)
    assert list == left + right
    assert -1 <= len(left) - len(right) <= 1
