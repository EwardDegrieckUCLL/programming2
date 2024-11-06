import pytest
from parentheses import matching_parentheses

@pytest.mark.parametrize('string', [
    ('((()))'),
    ('(()())'),
    ('()()()(())()')
])

def test_parentheses1(string):
    assert matching_parentheses(string), f"{string} should return True"


@pytest.mark.parametrize('string', [
    ('()('),
    (')('),
    (')()('),
    ('))(('),
    (')(())()')
])
def test_parentheses2(string):
    assert not matching_parentheses(string), f"{string} should return False"


