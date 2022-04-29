import pytest
import os
from hw4 import KeyValueStorage


@pytest.mark.parametrize("a, expected_result",
                         [('name', 'kek'),
                          ('mob', 'chikibambony'),
                          ('entity', 'slime'),
                          ('ios', 'mac'),
                          ('ms', 'windows 11'),
                          ('meme', 'aboba'),
                          ('power', '9001'),
                          ('song', 'shadilay')])
def test_KeyValueStorage_attributes(a, expected_result):
    path = 'temp.txt'
    file = open(path, 'x')
    file.write(a + '=' + expected_result)
    file.close()

    storage = KeyValueStorage(path)

    assert storage.__getattribute__(a) == expected_result
    os.remove(path)


@pytest.mark.parametrize("a, expected_result",
                         [('name', 'kek'),
                          ('mob', 'chikibambony'),
                          ('entity', 'slime'),
                          ('ios', 'mac'),
                          ('ms', 'windows 11'),
                          ('meme', 'aboba'),
                          ('power', '9001'),
                          ('song', 'shadilay')])
def test_KeyValueStorage_dict(a, expected_result):
    path = 'temp.txt'
    file = open(path, 'x')
    file.write(a + '=' + expected_result)
    file.close()

    storage = KeyValueStorage(path)

    assert storage[a] == expected_result
    os.remove(path)
