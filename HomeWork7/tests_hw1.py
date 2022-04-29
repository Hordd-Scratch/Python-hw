import pytest
from hw1 import find_occurrences

test_tree = {
    "first": ["RED", "BLUE"],
    "second": {
        "simple_key": ["simple", "list", "of", "RED", "valued"],
    },
    "third": {
        "abc": "BLUE",
        "jhl": "RED",
        "complex_key": {
            "key1": "value1",
            "key2": "RED",
            "key3": ["a", "lot", "of", "values", {"nested_key": "RED"}],
        }
    },
    "fourth": "RED",
}


@pytest.mark.parametrize("a, expected_result",
                         [('RED', 6),
                          ('BLUE', 2),
                          ('simple', 1),
                          ('list', 1),
                          ('of', 2),
                          ('valued', 1),
                          ('value1', 1),
                          ('a', 1),
                          ('lot', 1),
                          ('values', 1),
                          ('void1', 0),
                          ('void2', 0)])
def test_find_occurrences_good(a, expected_result):
    assert find_occurrences(test_tree, a) == expected_result


@pytest.mark.parametrize("a, expected_result",
                         [('RED', 1),
                          ('BLUE', 4),
                          ('simple', 6),
                          ('list', 4),
                          ('of', 3),
                          ('valued', 0),
                          ('value1', 0),
                          ('a', 11),
                          ('lot', 15),
                          ('values', 2),
                          ('void1', 5),
                          ('void2', 2)])
def test_find_occurrences_bad(a, expected_result):
    assert find_occurrences(test_tree, a) != expected_result