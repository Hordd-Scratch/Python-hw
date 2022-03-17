import pytest

from hw1 import get_file_data, \
    get_longest_diverse_words, \
    get_rarest_char, \
    count_punctuation_chars, \
    count_non_ascii_chars, \
    get_most_common_non_ascii_char


@pytest.mark.parametrize("a, expected_result",
                         [("TestFile_hw1.txt", ['jcasgnemvtk',
                                            'qwertyui',
                                            'habrhabfiao',
                                            'dpokfmpot',
                                            'oioutijjp',
                                            'ejduge',
                                            'akvnt',
                                            'hotuh',
                                            'uht',
                                            'fvb'])])
def test_get_longest_diverse_words(a, expected_result):
    assert get_longest_diverse_words(a) == expected_result


@pytest.mark.parametrize("a, expected_result",
                         [("TestFile_hw1.txt", 's')])
def test_get_rarest_char(a, expected_result):
    assert get_rarest_char(a) == expected_result


@pytest.mark.parametrize("a, expected_result",
                         [("TestFile_hw1.txt", 8)])
def test_count_punctuation_chars(a, expected_result):
    assert count_punctuation_chars(a) == expected_result


@pytest.mark.parametrize("a, expected_result",
                         [("TestFile_hw1.txt", 0)])
def test_count_non_ascii_chars(a, expected_result):
    assert count_non_ascii_chars(a) == expected_result


@pytest.mark.parametrize("a, expected_error",
                         [("TestFile_hw1.txt", IndexError)])
def test_get_most_common_non_ascii_char(a, expected_error):
    with pytest.raises(expected_error):
        get_most_common_non_ascii_char(a)
