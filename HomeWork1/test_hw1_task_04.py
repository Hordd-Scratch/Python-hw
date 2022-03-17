import pytest

from hw1_task_04 import check_sum_of_four


@pytest.mark.parametrize("a, b, c, d, expected_result",
                         [([0, 0], [0, 0], [0, 0], [0, 0], 16),
                          ([0, 1], [0, 0], [1, 0], [0, 0], 4),
                          ([0, 1], [0, -1], [1, 0], [0, 0], 6)])
def test_result_values(a, b, c, d, expected_result):
    assert check_sum_of_four(a, b, c, d) == expected_result


@pytest.mark.parametrize("a, b, c, d, expected_exception",
                         [([0, "fjd"], [0, 0], [0, 0], [0, 0], TypeError),
                          ([0, 1], [0, '0'], [1, 'j'], [0, 0], TypeError)])
def test_result_errors(a, b, c, d, expected_exception):
    with pytest.raises(expected_exception):
        check_sum_of_four(a, b, c, d)
