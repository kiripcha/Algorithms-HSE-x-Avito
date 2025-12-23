import pytest
import random
from src.compare import mergesort, quicksort


def create_sorted_array(n: int): return list(range(n))
def create_reverse_sorted_array(n: int): return list(range(n, 0, -1))
def create_almost_sorted_array(n: int):
    arr = list(range(n))
    for i in range(0, n, max(1, n // 100)):
        if i + 1 < n:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
    return arr
def create_random_array(n: int):
    arr = list(range(n))
    random.shuffle(arr)
    return arr
def create_array_with_duplicates(n: int):
    return [42] * n
def create_two_elements_swapped(n: int):
    arr = list(range(n))
    arr[0], arr[-1] = arr[-1], arr[0]
    return arr


# === Корректность ===
@pytest.mark.parametrize("size", [10_000, 50_000, 100_000])
def test_mergesort_correctness(size):
    data = create_random_array(size)
    expected = sorted(data)
    arr = data.copy()
    mergesort(arr)
    assert arr == expected


@pytest.mark.parametrize("size", [10_000, 50_000, 100_000])
def test_quicksort_correctness(size):
    data = create_random_array(size)
    expected = sorted(data)
    arr = data.copy()
    quicksort(arr)
    assert arr == expected


# === Маленькие случаи ===
@pytest.mark.parametrize("sort_func,name", [(mergesort, "mergesort"), (quicksort, "quicksort")])
@pytest.mark.parametrize("input_data, expected", [
    ([], []),
    ([1], [1]),
    ([3, 1], [1, 3]),
    ([5, 5, 5], [5, 5, 5]),
    ([-1, 10, 0], [-1, 0, 10]),
])
def test_small_cases(sort_func, name, input_data, expected):
    arr = input_data.copy()
    if name == "quicksort":
        sort_func(arr)
    else:
        sort_func(arr)
    assert arr == expected


# === Производительность и разница во времени ===
def test_already_sorted_large():
    arr1 = create_sorted_array(1_000)
    arr2 = arr1.copy()
    print("\n=== Уже отсортированный (150k) ===")
    mergesort(arr1)
    quicksort(arr2)

def test_reverse_sorted_large():
    arr1 = create_reverse_sorted_array(15_000)
    arr2 = arr1.copy()
    print("\n=== Обратно отсортированный (150k) ===")
    mergesort(arr1)
    quicksort(arr2)

def test_almost_sorted_large():
    arr1 = create_almost_sorted_array(2_000)
    arr2 = arr1.copy()
    print("\n=== Почти отсортированный (200k) ===")
    mergesort(arr1)
    quicksort(arr2)

def test_duplicates_extreme():
    arr1 = create_array_with_duplicates(2_000)
    arr2 = arr1.copy()
    print("\n=== Все элементы одинаковые (200k) ===")
    mergesort(arr1)
    quicksort(arr2)

def test_random_large():
    arr1 = create_random_array(1_000)
    arr2 = arr1.copy()
    print("\n=== Случайный массив (150k) ===")
    mergesort(arr1)
    quicksort(arr2)

def test_very_large_array():
    n = 300_000
    arr1 = create_random_array(n)
    arr2 = arr1.copy()
    print(f"\n=== Очень большой массив ({n}) ===")
    mergesort(arr1)
    quicksort(arr2)