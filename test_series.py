from series import *


def test_valid_n_fibonacci():
    actual = fibonacci(8)
    expected = 21
    assert expected == actual


def test_less_than_two_fibonacci():
    actual = fibonacci(1)
    expected = 1
    assert expected == actual


# FIBONACCI TESTS
# 1 test a working instance
# 2 test an instance of n=0

def test_valid_n_lucas():
    actual = lucas(8)
    expected = 29
    assert expected == actual


def test_n_is_one_lucas():
    actual = lucas(1)
    expected = 2
    assert expected == actual


def test_n_is_two_lucas():
    actual = lucas(2)
    expected = 1
    assert expected == actual

# LUCAS TESTS
# 1 test a working instance
# 2 test an instance of n=1
# 3 test an instance of n=2



# SUM TESTS
