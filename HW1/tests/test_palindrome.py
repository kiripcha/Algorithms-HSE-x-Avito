import pytest
from src.palindrome import is_palindrome

@pytest.mark.parametrize("num, expected", [
    (121, True),      # Классический палиндром
    (1221, True),     # Четное количество цифр
    (12321, True),    # Нечетное количество цифр
    (7, True),        # Однозначное число
    (11, True),       # Двузначный палиндром
    (99, True),       # Двузначный палиндром
    (1001, True),     # С нулями внутри
    (1111111111, True),  # Длинный палиндром
])
def test_palindromes(num, expected):
    assert is_palindrome(num) == expected

# Тесты на не-палиндромы
@pytest.mark.parametrize("num, expected", [
    (123, False),     # Обычное число
    (10, False),      # Двузначное не-палиндром
    (100, False),     # С нулями
    (1234, False),    # Четное количество
    (12345, False),   # Нечетное количество
    (1111111112, False),  # Почти палиндром, но нет
])
def test_non_palindromes(num, expected):
    assert is_palindrome(num) == expected

# def test_zero():
#     assert is_palindrome(0) == True  # 0 можно считать палиндромом, хотя не положительное

def test_negative_numbers():
    assert is_palindrome(-121) == False  # Отрицательное
    assert is_palindrome(-1) == False
    assert is_palindrome(-0) == False  # -0 == 0, но все равно False по логике

def test_single_digit():
    for i in range(1, 10):  # 0 проверен отдельно
        assert is_palindrome(i) == True

def test_two_digits_palindrome_edge():
    assert is_palindrome(10) == False  # Не палиндром
    assert is_palindrome(11) == True
    assert is_palindrome(99) == True
    assert is_palindrome(98) == False

def test_with_leading_zeros_effect():
    # Поскольку это int, ведущие нули не существуют, но проверим числа вроде 1001
    assert is_palindrome(1001) == True
    assert is_palindrome(1010) == False  # Не палиндром

def test_large_numbers():
    # Python поддерживает большие int, так что нет переполнения
    large_palindrome = 1234567890987654321
    assert is_palindrome(large_palindrome) == True
    
    large_non_palindrome = 1234567890987654322
    assert is_palindrome(large_non_palindrome) == False

def test_max_int_like():
    # Имитируем большие числа, близкие к пределам других языков, но в Python ок
    assert is_palindrome(2147447412) == True  # Палиндром около 2^31
    assert is_palindrome(2147483647) == False  # max int32

def test_power_of_ten():
    assert is_palindrome(1) == True
    assert is_palindrome(10) == False
    assert is_palindrome(100) == False
    assert is_palindrome(1000) == False

def test_all_same_digits():
    assert is_palindrome(111) == True
    assert is_palindrome(1111) == True
    assert is_palindrome(112) == False

def test_alternating_digits():
    assert is_palindrome(12121) == True
    assert is_palindrome(1212) == False

# Тест на нулевое число в середине
def test_zero_in_middle():
    assert is_palindrome(12021) == True
    assert is_palindrome(1202) == False  # Не палиндром

# Тест на минимальные и максимальные значения
def test_min_positive():
    assert is_palindrome(1) == True

# Если нужно больше тестов, можно добавить parametrize для большего покрытия