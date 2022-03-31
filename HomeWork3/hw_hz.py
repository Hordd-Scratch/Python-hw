# In previous homework task 4, you wrote a cache function that remembers other function output value.
# Modify it to be a parametrized decorator, so that the following code::
from typing import Any, List, Callable


def cache(times: int = 1) -> Callable:
    # Modified decorator
    def decorate_func(func: Callable) -> Callable:
        i = times
        # empty variable
        res = None

        def cached_func(*args: List[Any]) -> Any:
            # "nonlocal" in order to use a variable from an external non-global function
            nonlocal i
            nonlocal res
            if i == times:
                res = func(*args)
                i = 0
            else:
                i += 1
            return res

        return cached_func

    return decorate_func


@cache(times=2)
def square(a: float, b: float) -> str:
    return (a ** b) ** 2

