"""
Given a list of integers numbers "nums".

You need to find a sub-array with length less equal to "k", with maximal sum.

The written function should return the sum of this sub-array.

Examples:
    nums = [1, 3, -1, -3, 5, 3, 6, 7], k = 3
    result = 16
"""
from typing import List


# From the list of integers "nums", the function finds a sub-array of length k with the maximum sum
def find_maximal_subarray_sum(nums: List[int], k: int) -> int:
    max_sum = 0
    for i in range(len(nums) - k + 1):
        sub_sum = sum(nums[i:k+i])
        if sub_sum > max_sum:
            max_sum = sub_sum
    return max_sum
