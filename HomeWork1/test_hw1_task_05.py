import pytest

from hw1_task_05 import find_maximal_subarray_sum


@pytest.mark.parametrize("a, b, expected_result",
                         [([0, 0, 5, 6, 3, 6, 1, 1, 2, 5], 3, 15),
                          ([0, 1, 3, 0, -1, -6, -2, 8, 0, 3], 4, 9),
                          ([0, 1, 1.1, 2.4, 4.6, 3.2, 5.55, 4.7, 7, 3.0], 2, 11.7)])
def test_result_values(a, b, expected_result):
    assert find_maximal_subarray_sum(a, b) == expected_result


@pytest.mark.parametrize("a, b, expected_exception",
                         [([0, 0, 5, "6", 3, 6, 1, 1, 2, 5], 3, TypeError),
                          ([0, 1, 3, 0, -1, '7', -2, 8, 0, 3], 4, TypeError)])
def test_result_errors(a, b, expected_exception):
    with pytest.raises(expected_exception):
        find_maximal_subarray_sum(a, b)
