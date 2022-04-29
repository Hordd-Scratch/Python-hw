"""
Write a context manager, that suppresses passed exception.
Do it both ways: as a class and as a generator.

"""
from contextlib import contextmanager


# 'with' searches for 'yield' in all executable code and inserts the code written in it in its place
# 'contextmanager' converts function for 'with'
@contextmanager
def supressor(*args: any):
    try:
        yield
    except args:
        pass


with supressor(IndexError):
    [][2]
