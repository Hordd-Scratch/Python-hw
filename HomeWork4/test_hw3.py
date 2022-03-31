import pytest
from hw3 import my_precious_logger


@pytest.mark.parametrize("text",
                         ["error: file not found",
                          "error: aboba",
                          "error: error"])
def test_my_precious_logger_err(text, capsys):
    my_precious_logger(text)
    out, err = capsys.readouterr()
    assert err == text + "\n"


@pytest.mark.parametrize("text",
                         ["eor: filund",
                          "OK",
                          "kjrgblauebg"])
def test_my_precious_logger_out(text, capsys):
    my_precious_logger(text)
    out, err = capsys.readouterr()
    assert out == text + "\n"
