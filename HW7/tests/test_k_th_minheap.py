import pytest
from src.k_th_minheap import kth_largest_manual, kth_largest_heapq, MinHeap

@pytest.mark.parametrize(
    "func",
    [kth_largest_manual, kth_largest_heapq]
)
@pytest.mark.parametrize(
    "nums, k, expected",
    [
        ([3, 2, 1, 5, 6, 4], 2, 5),                    # Пример 1
        ([3, 2, 3, 1, 2, 4, 5, 5, 6], 4, 4),            # Пример 2
        ([1], 1, 1),                                   # Один элемент
        ([7, 7, 7, 7], 1, 7),                          # Все одинаковые, k=1
        ([7, 7, 7, 7], 3, 7),                          # Все одинаковые, любой k
        ([1, 2, 3, 4, 5], 1, 5),                       # k=1 → максимум
        ([1, 2, 3, 4, 5], 5, 1),                       # k=n → минимум
        ([-1, -5, -3, -4], 2, -3),                     # Отрицательные числа
        ([0, 0, 0, 0], 2, 0),                          # Нули
        ([10, 9, 8, 7, 6, 5, 4, 3, 2, 1], 3, 8),       # Убывающий порядок
        (list(range(100)), 50, 49),                    # Большой возрастающий
        ([100] * 1000 + [101], 1, 101),                # k=1 с выбросом
        ([1, 2, 2, 3, 3, 3, 4], 3, 3),                 # Много дубликатов
        ([5, 1, 5, 1, 5], 3, 5),                       # Чередование
    ]
)
def test_kth_largest_correctness(func, nums, k, expected):
    assert func(nums[:], k) == expected  # копия, чтобы не мутировать оригинал


def test_both_implementations_consistency():
    import random
    nums = [random.randint(-1000, 1000) for _ in range(1000)]
    for k in [1, 10, 100, 500, 999, 1000]:
        assert kth_largest_manual(nums[:], k) == kth_largest_heapq(nums[:], k)


def test_invalid_inputs():
    for func in [kth_largest_manual, kth_largest_heapq]:
        with pytest.raises(ValueError):
            func([], 1)
        with pytest.raises(ValueError):
            func([1, 2, 3], 0)
        with pytest.raises(ValueError):
            func([1, 2, 3], 4)


def test_large_input_performance():
    import random
    n = 100_000
    nums = [random.randint(-10**9, 10**9) for _ in range(n)]
    k = 42

    # Оба должны отработать без ошибок и дать одинаковый результат
    res1 = kth_largest_manual(nums[:], k)
    res2 = kth_largest_heapq(nums[:], k)
    assert res1 == res2

    # Проверка корректности через сортировку (только для уверенности)
    expected = sorted(nums, reverse=True)[k - 1]
    assert res1 == expected


def test_heapq_edge_cases():
    # heapq корректно работает с одинаковыми элементами
    assert kth_largest_heapq([5, 5, 5, 5], 2) == 5
    assert kth_largest_heapq([1, 100, 1, 100], 2) == 100


def test_manual_heap_edge_cases():
    # Проверка, что наша min-heap правильно поддерживает размер k
    heap = MinHeap()
    for x in [3, 1, 4, 1, 5, 9]:
        heap.push(x)
        if heap.size() > 3:
            heap.pop()
    assert heap.peek() == 4  # 3-е по величине: 9,5,4 → 4