from mystatistics import average
import pytest
from pytest import approx

@pytest.mark.parametrize('ns, expected', [
    ([0,1,2], 1),
    ([0.1, 0.1, 0.1], 0.1),
    ([1,1,1], 1),
    ([5], 5),
    ([1,5,3,4,8], 4.2)
])

def test_average(ns, expected):
    result = average(ns)
    assert approx(result, abs=0.01) == expected, f"Expected '{expected}', but result equals '{result}'"