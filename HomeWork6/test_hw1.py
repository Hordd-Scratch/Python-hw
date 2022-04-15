import pytest
from hw1 import User


@pytest.mark.parametrize("a, expected_result",
                         [(0, 0),
                          (1, 1),
                          (2, 2),
                          (10, 10)])
def test_class_user_good(a, expected_result):
    objs = []
    for i in range(a):
        objs.append(User())
    assert User.get_created_instances() == expected_result
    User.reset_instances_counter()


@pytest.mark.parametrize("a, expected_result",
                         [(9, 2),
                          (4, 5),
                          (7, 2),
                          (15, 10)])
def test_class_user_bad(a, expected_result):
    objs = []
    for i in range(a):
        objs.append(User())
    assert User.get_created_instances() != expected_result
    User.reset_instances_counter()
