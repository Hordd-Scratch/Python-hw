"""
Some of the functions have a bit cumbersome behavior when we deal with
positional and keyword arguments.

Write a function that accept any iterable of unique values and then
it behaves as range function:


import string


assert = custom_range(string.ascii_lowercase, 'g') == ['a', 'b', 'c', 'd', 'e', 'f']
assert = custom_range(string.ascii_lowercase, 'g', 'p') == ['g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o']
assert = custom_range(string.ascii_lowercase, 'p', 'g', -2) == ['p', 'n', 'l', 'j', 'h']

"""
import string
from typing import List


# The custom range function
def custom_range(str_symbols: string, *args: List[int]) -> List[any]:
    step = 1
    start_num = 0
    end_num = len(str_symbols)
    if len(args) == 1:
        end_num = str_symbols.index(args[0])
    elif len(args) >= 2:
        start_num = str_symbols.index(args[0])
        end_num = str_symbols.index(args[1])
        if len(args) == 3:
            step = args[2]
    return [str_symbols[i] for i in range(start_num, end_num, step)]