import pytest
from hw_hz import square


@pytest.mark.parametrize(
    "value",
    [
        (2, 2),
        (4, 5),
        (3, 4),
        (5, 3),
        (3, 6),
        (5, 8),
        (4, 6),
        (6, 2),
        (5, 9)
    ])
def test_cache(value: int):
    # Cache decorator with cache's maxsize arg test.
    actual_result = square(*value)
    square(*value)
    expected_result = square(*value)
    assert actual_result is expected_result
