import pytest
from hw_hz import square


@pytest.mark.parametrize("value",
                         [(3, 9),
                          (2, 4),
                          (5, 25),
                          (10, 100),
                          (15, 225)])
def test_square(a, expected_result):
    assert square(a) == expected_result
    pass
