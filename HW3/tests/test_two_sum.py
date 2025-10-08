import pytest
from src.two_sum import two_sum

def test_example_1():
    '''arr = [1, 3, 4, 10], k = 7'''
    arr = [1, 3, 4, 10]
    k = 7
    assert two_sum(arr, k) == [1, 2]

def test_example_2():
    '''arr = [5, 5, 1, 4], k = 10'''
    arr = [5, 5, 1, 4]
    k = 10
    assert two_sum(arr, k) == [0, 1]

def test_negative_numbers():
    '''с отрицательными числами'''
    arr = [-1, 2, -3, 4]
    k = -4
    assert two_sum(arr, k) == [0, 2]

def test_single_pair():
    '''массив с двумя элементами'''
    arr = [3, 7]
    k = 10
    assert two_sum(arr, k) == [0, 1]

def test_large_numbers():
    '''с большими числами'''
    arr = [100000, 200000, 300000, 400000]
    k = 500000
    assert two_sum(arr, k) == [1, 2]

def test_zero_sum():
    '''с суммой, равной нулю'''
    arr = [-5, 5, 10, -5]
    k = 0
    assert two_sum(arr, k) == [0, 1]