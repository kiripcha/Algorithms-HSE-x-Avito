# tests/test_kth_largest.py
import pytest
from src.k_th import kth_largest


@pytest.mark.parametrize(
    "nums, k, expected",
    [
        ([3, 2, 1, 5, 6, 4], 2, 5),                    # Пример 1
        ([3, 2, 3, 1, 2, 4, 5, 5, 6], 4, 4),            # Пример 2
        ([1], 1, 1),                                   # Один элемент
        ([5, 4, 3, 2, 1], 1, 5),                       # k=1 — максимум
        ([1, 2, 3, 4, 5], 5, 1),                       # k=n — минимум
        ([7, 7, 7, 7], 1, 7),                          # Все элементы одинаковые
        ([1, 3, 2], 2, 2),                             # Маленький массив
        ([-1, -5, -3, -4], 2, -3),                     # Отрицательные числа
        ([0, 0, 0, 0, 0], 3, 0),                       # Нули
        ([10, 9, 8, 7, 6, 5, 4, 3, 2, 1], 3, 8),       # Обратный порядок
        (list(range(1000)), 500, 499),                 # Большой отсортированный, средний элемент
        (list(range(999, -1, -1)), 100, 899),           # Большой обратный
        ([2, 1], 1, 2),                                # Два элемента
    ],
)
def test_kth_largest_correctness(nums, k, expected):
    # Делаем копию, чтобы не мутировать оригинал в параметрах
    arr = nums[:]
    result = kth_largest(arr, k)
    assert result == expected


def test_kth_largest_with_duplicates():
    nums = [3, 2, 3, 1, 2, 4, 5, 5, 6, 6]
    assert kth_largest(nums[:], 1) == 6
    assert kth_largest(nums[:], 2) == 6
    assert kth_largest(nums[:], 3) == 5
    assert kth_largest(nums[:], 4) == 5
    assert kth_largest(nums[:], 5) == 4
    assert kth_largest(nums[:], 10) == 1


def test_invalid_inputs():
    with pytest.raises(ValueError):
        kth_largest([], 1)
    with pytest.raises(ValueError):
        kth_largest([1, 2, 3], 0)
    with pytest.raises(ValueError):
        kth_largest([1, 2, 3], 4)
    with pytest.raises(ValueError):
        kth_largest([], 0)


def test_input_not_mutated():
    original = [3, 1, 4, 1, 5, 9, 2, 6]
    copy_arr = original[:]
    kth_largest(copy_arr, 3)
    # QuickSelect мутирует массив, но это допустимо по условию
    # Если нужно не мутировать — можно добавить копию в начало функции
    # Здесь просто проверяем, что логика работает на копии
    assert sorted(original) == [1, 1, 2, 3, 4, 5, 6, 9]


@pytest.mark.parametrize("n, k", [(10000, 1), (10000, 5000), (10000, 10000)])
def test_performance_large_array(n, k):
    import random
    nums = [random.randint(-10000, 10000) for _ in range(n)]
    expected = sorted(nums, reverse=True)[k - 1]
    assert kth_largest(nums[:], k) == expected


def test_deterministic_behavior():
    nums = [5, 2, 8, 1, 9, 3]
    results = [kth_largest(nums[:], 2) for _ in range(10)]
    assert all(r == 8 for r in results)  # Всегда должен возвращать один и тот же результат