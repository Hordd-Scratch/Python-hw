import os
import pytest
from pathlib import Path
from hw6 import universal_file_counter

test_dir = Path("C:\\Users\\Horrd\\PycharmProjects\\Python-hw\\HomeWork7")


@pytest.mark.parametrize("a, b, c, expected_result",
                         [(test_dir, "txt", str.split, 10),
                          (test_dir, "txt", None, 2),
                          (test_dir, "py", str.split, 1648),
                          (test_dir, "py", None, 491)])
def test_universal_file_counter_three_parameters(a, b, c, expected_result):
    assert universal_file_counter(a, b, c) == expected_result
