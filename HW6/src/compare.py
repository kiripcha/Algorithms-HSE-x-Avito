import time
from typing import List, Callable, Any
import sys

# Увеличиваем лимит рекурсии (нужно для больших массивов)
sys.setrecursionlimit(100_000)


def timer(func: Callable) -> Callable:
    """Декоратор для замера времени выполнения функции"""
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"{func.__name__}: {end - start:.6f} s")
        return result
    return wrapper


def merge(arr: List[Any], left: List[Any], right: List[Any]) -> None:
    """Правильное слияние двух отсортированных массивов в arr"""
    i = j = k = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    # Копируем оставшиеся элементы
    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1
    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1


@timer
def mergesort(arr: List[Any]) -> None:
    """Рекурсивная сортировка слиянием (in-place через временные массивы)"""
    if len(arr) <= 1:
        return

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    # Рекурсивно сортируем половины
    mergesort(left)
    mergesort(right)

    # Сливаем обратно в оригинальный arr
    merge(arr, left, right)


@timer
def quicksort(arr: List[Any], low: int = 0, high: int = None) -> None:
    """Рекурсивная быстрая сортировка с медианой трёх"""
    if high is None:
        high = len(arr) - 1

    def partition(l: int, r: int) -> int:
        # Медиана трёх
        mid = (l + r) // 2
        if arr[mid] < arr[l]:
            arr[mid], arr[l] = arr[l], arr[mid]
        if arr[r] < arr[l]:
            arr[r], arr[l] = arr[l], arr[r]
        if arr[r] < arr[mid]:
            arr[r], arr[mid] = arr[mid], arr[r]
        # Перемещаем опорный в конец
        arr[mid], arr[r] = arr[r], arr[mid]
        pivot = arr[r]

        i = l - 1
        for j in range(l, r):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[r] = arr[r], arr[i + 1]
        return i + 1

    if low < high:
        pi = partition(low, high)
        quicksort(arr, low, pi - 1)
        quicksort(arr, pi + 1, high)