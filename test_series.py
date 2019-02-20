from series import *


def test_valid_n_fibonacci():
    actual = fibonacci(8)
    expected = 21
    assert expected == actual


def test_less_than_two_fibonacci():
    actual = fibonacci(1)
    expected = 0
    assert expected == actual


# FIBONACCI TESTS
# 1 test a working instance
# 2 test an instance of n=1

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
# 1 test a working instance > 2
# 2 test an instance of n=1
# 3 test an instance of n=2


# def test_requred_parameters_sum():
#     actual = sum_series(8)
#     expected = 21
#     assert expected == actual


# def test_requred_parameters_sum():
#     actual = sum_series(8, 2, 1)
#     expected = 21
#     assert expected == actual

# SUM TESTS
# 1 test with required parameter, fibonacci
# 2 test with required and optional parameters, fibonacci
# 3 test with required and optional parameters, lucas
# 4 test with required parameter and optional parameters, alternate
