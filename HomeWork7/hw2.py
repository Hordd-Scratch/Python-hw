"""
Given two strings. Return if they are equal when both are typed into
empty text editors. # means a backspace character.
Note that after backspacing an empty text, the text will continue empty.
Examples:
    Input: s = "ab#c", t = "ad#c"
    Output: True
    # Both s and t become "ac".
    Input: s = "a##c", t = "#a#c"
    Output: True
    Explanation: Both s and t become "c".
    Input: a = "a#c", t = "b"
    Output: False
    Explanation: s becomes "c" while t becomes "b".
"""


def backspace_compare(first: str, second: str) -> bool:
    first_temp = ''
    for char in first:
        if char == '#':
            if len(first_temp) > 0:
                first_temp = first_temp[:-1]
        else:
            first_temp += char
    second_temp = ''
    for char in second:
        if char == '#':
            if len(second_temp) > 0:
                second_temp = second_temp[:-1]
        else:
            second_temp += char
    return first_temp == second_temp
