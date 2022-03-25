import pytest
from hw_hz import is_armstrong


@pytest.mask.parametrise("a, expected", [(1, 1)])
def test_is_armstrong(a):
    return