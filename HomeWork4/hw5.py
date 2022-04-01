"""
Write a generator that takes a number N as an input
and returns a generator that yields N FizzBuzz numbers


Definition of done:
 - function is created
 - function is properly formatted
 - function has tests


# >>> list(fizzbuzz(5))
["1", "2", "fizz", "4", "buzz"]

* https://en.wikipedia.org/wiki/Fizz_buzz
"""
from typing import List, Generator


# A generator that takes a number N as an input and returns N FizzBuzz numbers*
def fizzbuzz(n: int) -> Generator[str, None, None]:
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            yield "FizzBuzz"
        elif i % 3 == 0:
            yield "Fizz"
        elif i % 5 == 0:
            yield "Buzz"
        else:
            yield str(i)
