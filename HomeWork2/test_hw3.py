import pytest
from hw3 import combinations


@pytest.mark.parametrize("a, expected_result",
                         [([[1, 2], [3, 4]], [[1, 3], [1, 4], [2, 3], [2, 4]]),
                          ([[1, 2], [3]], [[1, 3], [2, 3]]),
                          ([[1, 2], [8], [3, 4]], [[1, 8, 3], [1, 8, 4], [2, 8, 3], [2, 8, 4]])])
def test_result_values(a, expected_result):
    assert combinations(a) == expected_result


@pytest.mark.parametrize("a, expected_error",
                          [([[1, 2], 8, [3, 4]], TypeError)])
def test_result_errors(a, expected_error):
    with pytest.raises(expected_error):
        combinations(a)
