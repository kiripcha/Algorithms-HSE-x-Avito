import pytest
from src.max_even_sum import max_even_sum

@pytest.mark.parametrize("arr, expected", [
    ([5, 7, 13, 2, 14], 36),  # Пример 1: 2 + 7 + 13 + 14 = 36
    ([3], 0),                  # Пример 2: только нечётное, возвращаем 0
    ([2, 4, 6], 12),          # Все ч chётные: 2 + 4 + 6 = 12
    ([1, 3, 5], 0),           # Все нечётные, возвращаем 0
    ([2, 3, 4], 6),           # 2 + 4 = 6
    ([1, 2, 3, 4], 6),        # 2 + 4 = 6
    ([2], 2),                  # Одно чётное число
    ([1], 0),                  # Одно нечётное число
])
def test_basic_cases(arr, expected):
    assert max_even_sum(arr) == expected

# Пограничные тесты
def test_empty_array():
    assert max_even_sum([]) == 0  # Пустой массив

def test_all_same_even():
    assert max_even_sum([2, 2, 2, 2]) == 8  # Все 2: 2 + 2 + 2 + 2 = 8

def test_all_same_odd():
    assert max_even_sum([1, 1, 1, 1]) == 0  # Все нечётные, возвращаем 0

def test_large_numbers():
    assert max_even_sum([1000000, 2000000, 3]) == 3000000  # 1000000 + 2000000 = 3000000

def test_single_large_even():
    assert max_even_sum([1000000]) == 1000000  # Одно большое чётное число

def test_single_large_odd():
    assert max_even_sum([1000001]) == 0  # Одно большое нечётное число

def test_mixed_with_zeros():
    assert max_even_sum([0, 2, 3, 4]) == 6  # 0 + 2 + 4 = 6

def test_all_zeros():
    assert max_even_sum([0, 0, 0]) == 0  # Все нули, сумма 0

def test_maximum_subset():
    assert max_even_sum([1, 2, 3, 4, 5, 6]) == 12  # 2 + 4 + 6 = 12

def test_no_even_numbers():
    assert max_even_sum([1, 3, 5, 7, 9]) == 0  # Нет чётных чисел

def test_all_even_numbers():
    assert max_even_sum([2, 4, 6, 8]) == 20  # 2 + 4 + 6 + 8 = 20

def test_large_array():
    assert max_even_sum([2, 2, 2, 2, 3, 3, 3, 3]) == 8  # 2 + 2 + 2 + 2 = 8