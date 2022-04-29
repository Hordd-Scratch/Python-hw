"""
Given a dictionary (tree), that can contains multiple nested structures.
Write a function, that takes element and finds the number of occurrences
of this element in the tree.

Tree can only contains basic structures like:
    str, list, tuple, dict, set, int, bool
"""
from typing import Any, List, Tuple


def find_occurrences(tree: dict, element: Any) -> int:
    def find(root: any, counter: int) -> int:
        if isinstance(root, dict):
            nodes = root.values()
        elif isinstance(root, List) or isinstance(root, Tuple):
            nodes = root
        for node in nodes:
            if node == element:
                counter += 1
            if isinstance(node, dict) or isinstance(node, List) or isinstance(node, Tuple):
                counter = find(node, counter)
        return counter

    return find(tree, 0)
