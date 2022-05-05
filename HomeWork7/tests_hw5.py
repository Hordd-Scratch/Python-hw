import pytest
import os
from hw5 import merge_sorted_files



@pytest.mark.parametrize("a, expected_result",
                         [([[1, 4, 7], [2, 5, 8], [3, 6, 9]], [1, 2, 3, 4, 5, 6, 7, 8, 9]),
                          ([[23, 43, 12], [32, 34, 45], [56, 67, 78]], [12, 23, 32, 34, 43, 45, 56, 67, 78]),
                          ([[23, 45, 54], [56, 56, 32], [45, 16, 84]], [16, 23, 32, 45, 45, 54, 56, 56, 84]),
                          ([[6, 5, 1678], [518, 35, 48], [51, 783, 516]], [5, 6, 35, 48, 51, 516, 518, 783, 1678]),
                          ([[87, 25, 6], [98, 75], [69, 95, 68, 72, 90]], [6, 25, 68, 69, 72, 75, 87, 90, 95, 98]),
                          ([[9, 823, 764368], [17], [6591, 876, 581, 75]], [9, 17, 75, 581, 823, 876, 6591, 764368]),
                          ([[96, 79], [348, 76, 2093, 486, 284], [36]], [36, 76, 79, 96, 284, 348, 486, 2093]),
                          ([[11, 1, 222], [33, 34, 4], [45, 55, 66, 6]], [1, 4, 6, 11, 33, 34, 45, 55, 66, 222])])
def test_merge_sorted_files(a, expected_result):
    path = ['temp1.txt', 'temp2.txt', 'temp3.txt']
    for i in range(3):
        file = open(path[i], 'x')
        for j in a[i]:
            file.write(str(j) + '\n')
        file.close()

    assert list(merge_sorted_files([path[0], path[1], path[2]])) == expected_result
    for i in range(3):
        os.remove(path[i])
