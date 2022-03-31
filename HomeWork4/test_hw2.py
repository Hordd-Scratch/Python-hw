import pytest
import os
from hw2 import read_magic_number


@pytest.mark.parametrize("a, expected_result",
                         [('2', True),
                          ('1', True),
                          ('2.5', True),
                          ('1.45', True),
                          ('2.99999', True),
                          ('1.001', True),
                          ('1.999', True)])
def test_read_magic_number_good(a, expected_result):
    path = 'temp.txt'
    file = open(path, 'x')
    file.write(a)
    file.close()
    assert read_magic_number(path) == expected_result
    os.remove(path)


@pytest.mark.parametrize("a, expected_result",
                         [('3', False),
                          ('0', False),
                          ('8.5', False),
                          ('0.45', False),
                          ('3.99999', False),
                          ('0.001', False),
                          ('0.999', False)])
def test_read_magic_number_bad(a, expected_result):
    path = 'temp.txt'
    file = open(path, 'x')
    file.write(a)
    file.close()
    assert read_magic_number(path) == expected_result
    os.remove(path)
