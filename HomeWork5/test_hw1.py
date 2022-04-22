import pytest
from hw1 import Teacher, Student


@pytest.mark.parametrize("a, expected_result",
                         [('qwerty', 'qwerty'),
                          ('asdfg', 'asdfg'),
                          ('zxcvb', 'zxcvb'),
                          ('amogus', 'amogus'),
                          ('Vova', 'Vova')])
def test_Teachers_last_name_good(a, expected_result):
    teacher = Teacher('Shadrin', a)
    assert teacher.last_name == expected_result


@pytest.mark.parametrize("a, expected_result",
                         [('q5werty', 'qwerty'),
                          ('a5sdfg', 'asdfg'),
                          ('z5xcvb', 'zxcvb'),
                          ('a5mogus', 'amogus'),
                          ('V5ova', 'Vova')])
def test_Teachers_last_name_bad(a, expected_result):
    teacher = Teacher('Shadrin', a)
    assert teacher.last_name != expected_result

@pytest.mark.parametrize("a, expected_result",
                         [('qwerty', 'qwerty'),
                          ('asdfg', 'asdfg'),
                          ('zxcvb', 'zxcvb'),
                          ('amogus', 'amogus'),
                          ('Vova', 'Vova')])
def test_Teachers_first_name_good(a, expected_result):
    teacher = Teacher(a, 'Shadrin')
    assert teacher.first_name == expected_result


@pytest.mark.parametrize("a, expected_result",
                         [('q5werty', 'qwerty'),
                          ('a5sdfg', 'asdfg'),
                          ('z5xcvb', 'zxcvb'),
                          ('a5mogus', 'amogus'),
                          ('V5ova', 'Vova')])
def test_Teachers_first_name_bad(a, expected_result):
    teacher = Teacher(a, 'Shadrin')
    assert teacher.first_name != expected_result


@pytest.mark.parametrize("a, expected_result",
                         [('qwerty', 'qwerty'),
                          ('asdfg', 'asdfg'),
                          ('zxcvb', 'zxcvb'),
                          ('amogus', 'amogus'),
                          ('Vova', 'Vova')])
def test_Student_last_name_good(a, expected_result):
    student = Student('Shadrin', a)
    assert student.last_name == expected_result


@pytest.mark.parametrize("a, expected_result",
                         [('q5werty', 'qwerty'),
                          ('a5sdfg', 'asdfg'),
                          ('z5xcvb', 'zxcvb'),
                          ('a5mogus', 'amogus'),
                          ('V5ova', 'Vova')])
def test_Student_last_name_bad(a, expected_result):
    student = Student('Shadrin', a)
    assert student.last_name != expected_result

@pytest.mark.parametrize("a, expected_result",
                         [('qwerty', 'qwerty'),
                          ('asdfg', 'asdfg'),
                          ('zxcvb', 'zxcvb'),
                          ('amogus', 'amogus'),
                          ('Vova', 'Vova')])
def test_Student_first_name_good(a, expected_result):
    student = Student(a, 'Shadrin')
    assert student.first_name == expected_result


@pytest.mark.parametrize("a, expected_result",
                         [('q5werty', 'qwerty'),
                          ('a5sdfg', 'asdfg'),
                          ('z5xcvb', 'zxcvb'),
                          ('a5mogus', 'amogus'),
                          ('V5ova', 'Vova')])
def test_Student_first_name_bad(a, expected_result):
    student = Student(a, 'Shadrin')
    assert student.first_name != expected_result


