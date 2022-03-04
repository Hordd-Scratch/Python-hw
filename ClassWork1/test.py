from typing import Tuple


def find_max_and_min(file_name: str) -> Tuple[int, int]:
    with open(file_name) as fi:
        l = [int(line) for line in fi]
    return min(l), max(l)


print(find_max_and_min("numbers"))
