import os
import pytest
from pathlib import Path
from hw6 import universal_file_counter


@pytest.mark.parametrize("a, b, c, expected_result",
                         [(Path("C:\\Users\\Horrd\\PycharmProjects\\Python-hw\\HomeWork7"), "txt", str.split, 10),
                          (Path("C:\\Users\\Horrd\\PycharmProjects\\Python-hw\\HomeWork7"), "txt", None, 2),
                          (Path("C:\\Users\\Horrd\\PycharmProjects\\Python-hw\\HomeWork7"), "py", str.split, 1645),
                          (Path("C:\\Users\\Horrd\\PycharmProjects\\Python-hw\\HomeWork7"), "py", None, 490)])
def test_universal_file_counter_three_parameters(a, b, c, expected_result):
    assert universal_file_counter(a, b, c) == expected_result
