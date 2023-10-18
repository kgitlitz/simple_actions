

from src.my_math_lib import simple_math_lib

def test_add():
    m = simple_math_lib

    expected = 6
    actual = m.add(1, 2, 3)

    assert expected == actual


def test_add_list():
    m = simple_math_lib

    nums = [2, 3, 4, 5]

    expected = sum(nums)
    actual = m.add(*nums)

    assert expected == actual

def test_multiply():

    m = simple_math_lib

    expected = 6
    actual = m.multiply(1, 2, 3)

    assert expected == actual

def test_multiply_list():
    m = simple_math_lib

    nums = [2, 3, 0, 5]

    expected = 0
    actual = m.multiply(*nums)

    assert expected == actual