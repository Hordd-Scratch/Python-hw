"""
Write a function that takes K lists as arguments and returns all possible
lists of K items where the first element is from the first list,
the second is from the second and so one.

You may assume that that every list contain at least one element

Example:

assert combinations([1, 2], [3, 4]) == [
    [1, 3],
    [1, 4],
    [2, 3],
    [2, 4],
]
"""
from typing import List, Any


# function that takes K lists as arguments and returns all possible lists of K items
def combinations(args: List[Any]) -> List[List]:
    a = iter(args)
    part = object()
    res = [[]]
    while True:
        temp = next(a, part)
        if temp == part:
            break
        res = [r + [i] for r in res for i in temp]
    return res


abc = [[1, 2], [3, 4], [5, 6]]
print(combinations(abc))
