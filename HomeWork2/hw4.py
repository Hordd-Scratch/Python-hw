"""
Write a function that accepts another function as an argument. Then it
should return such a function, so the every call to initial one
should be cached.


def func(a, b):
    return (a ** b) ** 2


cache_func = cache(func)

some = 100, 200

val_1 = cache_func(*some)
val_2 = cache_func(*some)

assert val_1 is val_2

"""
from functools import lru_cache


@lru_cache(maxsize=32)
def func(a, b):
    return (a ** b) ** 2

for i in range(10):
    print([func(n, n+1) for n in range(10)])

