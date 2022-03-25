import pytest
from hw_hz import is_armstrong


@pytest.mark.parametrize("a, expected_result",
                         [(9, True),
                          (153, True)])
def test_is_armstrong_good(a, expected_result):
    assert is_armstrong(a) == expected_result


@pytest.mark.parametrize("a, expected_result",
                         [(10, False),
                          (152, False)])
def test_is_armstrong_bad(a, expected_result):
    assert is_armstrong(a) == expected_result
