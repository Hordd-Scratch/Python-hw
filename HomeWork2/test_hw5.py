import pytest
import string
from hw5 import custom_range



@pytest.mark.parametrize("a, b, expected_result",
                         [(string.ascii_lowercase, 'g', ['a', 'b', 'c', 'd', 'e', 'f']),
                          (string.ascii_lowercase, 'b', ['a']),
                          (string.ascii_lowercase, 'k', ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'])])
def test_custom_range(a, b, expected_result):
    assert custom_range(a, b) == expected_result


@pytest.mark.parametrize("a, b, c, expected_result",
                         [(string.ascii_lowercase, 'g', 'p', ['g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o']),
                          (string.ascii_lowercase, 'c', 'i', ['c', 'd', 'e', 'f', 'g', 'h']),
                          (string.ascii_lowercase, 'w', 'z', ['w', 'x', 'y'])])
def test_custom_range(a, b, c, expected_result):
    assert custom_range(a, b, c) == expected_result


@pytest.mark.parametrize("a, b, c, d, expected_result",
                         [(string.ascii_lowercase, 'p', 'g', -2, ['p', 'n', 'l', 'j', 'h']),
                          (string.ascii_lowercase, 'y', 'b', -4, ['y', 'u', 'q', 'm', 'i', 'e']),
                          (string.ascii_lowercase, 'b', 'n', 2, ['b', 'd', 'f', 'h', 'j', 'l'])])
def test_custom_range(a, b, c, d, expected_result):
    assert custom_range(a, b, c, d) == expected_result
