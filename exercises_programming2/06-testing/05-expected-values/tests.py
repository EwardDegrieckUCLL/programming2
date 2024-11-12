import pytest
from mergesort import *
from itertools import permutations

@pytest.mark.parametrize('list', [
    list(range(k)) for k in range(101)
])

def test_split_in_two(list):
    left, right = split_in_two(list)
    assert list == left + right
    assert -1 <= len(left) - len(right) <= 1


@pytest.mark.parametrize('left', [
    list(range(k)) for k in range(16)
    ] 
    + [ [], [0,0,0,0], [100,100,105], [4, 10, 15]
])

@pytest.mark.parametrize('right', [
    list(range(k)) for k in range(21)
    ] 
    + [ [], [2,2,2,2,2], [1,1,2,2], [5, 18, 20]
])

def test_merge_sorted(left, right):
    result = merge_sorted(left, right)
    assert result == sorted(result)

    result = merge_sorted(right, left)
    assert result == sorted(result)

@pytest.mark.parametrize('sorted_list, permutations', [
    ([1,2,3,3,4,5], [permutations([1,2,3,3,4,5])] ),
    ([0,0,0,0], [[0,0,0,0]]),
    ([-1,20,25,30,30,135], [permutations([-1,20,25,30,30,135])] ),
])

def test_merge_sort(sorted_list, permutations):
    for permutation in permutations:
        assert sorted_list == merge_sort(permutation)