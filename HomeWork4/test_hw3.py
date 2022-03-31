import sys
import pytest
from hw3 import my_precious_logger


@pytest.mark.parametrize("text",
                         [("error: file not found")])
def test_my_precious_logger_stderr(text):
    ...


@pytest.mark.parametrize("text",
                         [("OK")])
def test_my_precious_logger_stdout(text):
    ...
