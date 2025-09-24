import pytest
from src.count_primes import count_primes

@pytest.mark.parametrize("n, expected", [
    (10, 4),    # Пример 1: 2, 3, 5, 7
    (1, 0),     # Пример 2: нет простых чисел
    (2, 0),     # Нет простых чисел меньше 2
    (3, 1),     # Только 2
    (20, 8),    # 2, 3, 5, 7, 11, 13, 17, 19
    (100, 25),  # Простых чисел меньше 100: 25
])
def test_basic_cases(n, expected):
    """Проверяет базовые случаи для функции count_primes"""
    assert count_primes(n) == expected

def test_negative_input():
    """Проверяет отрицательный ввод"""
    assert count_primes(-1) == 0
    assert count_primes(-10) == 0
    assert count_primes(-1000) == 0  # Большое отрицательное число
    assert count_primes(-1000000) == 0  # Очень большое отрицательное число

def test_zero_input():
    """Проверяет ввод нуля"""
    assert count_primes(0) == 0

def test_small_numbers():
    """Проверяет малые числа"""
    assert count_primes(4) == 2  # 2, 3
    assert count_primes(5) == 2  # 2, 3
    assert count_primes(6) == 3  # 2, 3, 5

def test_large_numbers():
    """Проверяет большие числа"""
    assert count_primes(1000) == 168  # Простых чисел меньше 1000
    assert count_primes(10000) == 1229  # Простых чисел меньше 10000
    assert count_primes(1000000) == 78498  # Простых чисел меньше 1_000_000
    assert count_primes(10000000) == 664579  # Простых чисел меньше 10_000_000

def test_boundary_cases():
    """Проверяет пограничные случаи около простых чисел"""
    assert count_primes(11) == 4  # 2, 3, 5, 7
    assert count_primes(12) == 5  # 2, 3, 5, 7, 11
    assert count_primes(13) == 5  # 2, 3, 5, 7, 11
    assert count_primes(14) == 6  # 2, 3, 5, 7, 11, 13

def test_single_prime():
    """Проверяет случаи с одним простым числом"""
    assert count_primes(3) == 1  # Только 2

def test_near_large_prime():
    """Проверяет числа, близкие к большим простым числам"""
    assert count_primes(1000003) == 78500  # 1000003 — простое
    assert count_primes(1000004) == 78501  # После простого 1000003

def test_extreme_large_numbers():
    """Проверяет очень большие числа, близкие к пределам int32"""
    assert count_primes(2147483647) == 105097565  # max int32 (2^31 - 1, простое)
    assert count_primes(2147483648) == 105097565  # После max int32

def test_transition_points():
    """Проверяет точки, где количество простых чисел увеличивается"""
    assert count_primes(17) == 7   # 2, 3, 5, 7, 11, 13, 17
    assert count_primes(18) == 7   # 2, 3, 5, 7, 11, 13, 17
    assert count_primes(19) == 8   # 2, 3, 5, 7, 11, 13, 17, 19

def test_very_small_changes():
    """Проверяет последовательные числа с малыми изменениями"""
    assert count_primes(101) == 25  # Простых чисел меньше 101
    assert count_primes(102) == 25  # Простых чисел меньше 102
    assert count_primes(103) == 26  # 101 — простое