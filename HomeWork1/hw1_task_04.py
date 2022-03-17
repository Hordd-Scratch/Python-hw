"""
Classic task, a kind of walnut for you

Given four lists A, B, C, D of integer values,
    compute how many tuples (i, j, k, l) there are such that A[i] + B[j] + C[k] + D[l] is zero.

We guarantee, that all A, B, C, D have same length of N where 0 ≤ N ≤ 1000.
"""
from typing import List
from random import randint


# Function the number of tuples (i, j, k, l) satisfying the condition A[i]+ B[j] + C[k] + D[l] = 0
def check_sum_of_four(a: List[int], b: List[int], c: List[int], d: List[int]) -> int:
    sums = {}
    for i in a:
        for j in b:
            if i + j not in sums:
                sums[i + j] = 1
            else:
                sums[i + j] += 1
    counter = 0
    for i in c:
        for j in d:
            if -1 * (i + j) in sums:
                counter += sums[-1 * (i + j)]
    return counter


# The function of filling the sheet with random numbers
def set_rand_list(a: list[int]) -> list[int]:
    for i in range(len(a)):
        a[i] = randint(-1000000, 1000000)
    return a


# Generating lists of the same length
n = randint(0, 1000)
A = [0 for i in range(n)]
B = A
C = A
D = A

# Setting random values in lists
A = set_rand_list(A)
B = set_rand_list(B)
C = set_rand_list(C)
D = set_rand_list(D)

print(check_sum_of_four(A, B, C, D))