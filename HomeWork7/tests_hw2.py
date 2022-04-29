import pytest
from hw2 import backspace_compare


@pytest.mark.parametrize("a, b",
                         [("ab#c", "ad#c"),
                          ("a##c", "#a#c"),
                          ("qww#erf#ty", "qwerty"),
                          ("af#bog#ba", "abobabnm###"),
                          ("cl#hil#l#kyl#baml#bony", "chikyl#bl#ambl#ol#ny"),
                          ("mid#nid#d#d#on", "md#ind#iod#n"),
                          ("bananabanana######", "banana######banana")])
def test_backspace_compare_good(a, b):
    assert backspace_compare(a, b)


@pytest.mark.parametrize("a, b",
                         [("aby#c", "ad#c"),
                          ("a#dy#c", "#a#c"),
                          ("qww#erf#ty", "qwterty"),
                          ("af#byog#ba", "aboybabnm###"),
                          ("cl#hil#l#kyly#baml#bony", "chikyly#bl#amblgg#ol#ny"),
                          ("mid#niyd#dgg#d#on", "mdgg#ind#iyod#n"),
                          ("bananyabgganana######", "bananay##gg####banana")])
def test_backspace_compare_bad(a, b):
    assert not backspace_compare(a, b)
