import pytest
from search import *

@pytest.mark.parametrize('students, target_id', [
    ([Student(x) for x in range(21)], -1),
    ([Student(x) for x in range(21)], 0),
    ([Student(x) for x in range(21)], 21),
    ([Student(x) for x in range(21)], 15),
    ([Student(x) for x in range(21) if x%2 == 0], 15),
    ([], 20)
])

def test_compare_searches(students, target_id):
    assert linear_search(students, target_id) == binary_search(students, target_id)