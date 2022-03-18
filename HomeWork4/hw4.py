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

# BAN
# def is_armstrong(number: int) -> int:
#     str_digits = str(number)
#     lenght_number = len(str_digits)
#     if sum([int(a)**lenght_number for a in str_digits]) == number:
#         return True
#     else:
#         return False


assert is_armstrong(153) == True, 'Is Armstrong number'
assert is_armstrong(10) == False, 'Is not Armstrong number'
