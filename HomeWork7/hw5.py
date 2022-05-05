# Write a function that merges integer from sorted files and returns an iterator
# file1.txt:
# 1
# 3
# 5
# file2.txt:
# 2
# 4
# 6
# >>> list(merge_sorted_files(["file1.txt", "file2.txt"]))
# [1, 2, 3, 4, 5, 6]
from pathlib import Path
from typing import List, Union, Iterator


def merge_sorted_files(file_list: List[Union[Path, str]]) -> Iterator:
    int_nums = []
    for file_path in file_list:
        with open(file_path) as file:
            for line in file:
                int_nums.append(int(line))
    for i in range(len(int_nums)):
        index = i
        for j in range(i + 1, len(int_nums)):
            if int_nums[j] < int_nums[index]:
                index = j
        int_nums[i], int_nums[index] = int_nums[index], int_nums[i]
    return iter(int_nums)
