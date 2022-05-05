# Write a function that takes directory path, a file extension and an optional tokenizer.
# It will count lines in all files with that extension if there are no tokenizer.
# If a the tokenizer is not none, it will count tokens.
# For dir with two files from hw1.py:
# >>> universal_file_counter(test_dir, "txt")
# 6
# >>> universal_file_counter(test_dir, "txt", str.split)
# 6
import os
from pathlib import Path
from typing import Optional, Callable


def universal_file_counter(dir_path: Path, file_extension: str, tokenizer: Optional[Callable] = None) -> int:
    result = 0
    for file_path in os.listdir(dir_path):
        split_path = file_path.split('.')
        if len(split_path) > 1:
            if split_path[1] == file_extension:
                with open(file_path) as file:
                    if tokenizer is None:
                        result += len(list(file))
                    else:
                        for line in list(file):
                            result += len(tokenizer(line))
    return result


print(universal_file_counter(Path("C:\\Users\\Horrd\\PycharmProjects\\Python-hw\\HomeWork7"), "txt"))
