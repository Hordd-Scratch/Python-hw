"""
Armstrong number is a number that is the sum of its own digits each raised to the power of the number of digits.
https://en.wikipedia.org/wiki/Narcissistic_number

Examples:

- 9 is an Armstrong number, 9 = 9^1 = 9
- 10 is not: 10 != 1^2 + 0^2 = 1
- 153 is : 153 = 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153


Write a function that detects if a number is Armstrong number in functionaly style:
 - use map or other utilities from functools library,
 - use anonymous functions (or use function as argument)
 - do not use loops, preferably using list comprehensions

### Example function signature and call
"""


def is_armstrong(number: int) -> int:
    list_str_digits = str(number)
    number_lenght = len(list_str_digits)
    list_digits = list(map(int, list_str_digits))

    def exponentiation(a: int) -> int:
        return a ** number_lenght

    list_digits = list(map(exponentiation, list_digits))
    sum_digits = sum(list_digits)
    if sum_digits == number:
        return True
    else:
        return False


assert is_armstrong(153) == True, 'Is Armstrong number'
assert is_armstrong(10) == False, 'Is not Armstrong number'
