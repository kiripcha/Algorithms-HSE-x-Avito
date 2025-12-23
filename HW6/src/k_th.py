from typing import List

def kth_largest(nums: List[int], k: int) -> int:
    """
    Находит k-ый по величине элемент в неотсортированном массиве.
    Использует алгоритм QuickSelect (вариант QuickSort с одной рекурсией).
    Средняя сложность O(n), худшая O(n²), но на практике работает отлично.
    """
    if not nums or k < 1 or k > len(nums):
        raise ValueError("Invalid input or k out of bounds")

    # Так как ищем k-ый по величине (k=1 — максимум), преобразуем в поиск (n-k)-го по возрастанию
    target_index = len(nums) - k

    left, right = 0, len(nums) - 1

    while left <= right:
        # Выбираем опорный элемент — последний в текущем отрезке
        pivot_index = partition(nums, left, right)

        if pivot_index == target_index:
            return nums[pivot_index]
        elif pivot_index < target_index:
            left = pivot_index + 1
        else:
            right = pivot_index - 1

    # Сюда не должны попасть при корректной реализации
    raise RuntimeError("Unexpected error in QuickSelect")


def partition(arr: List[int], low: int, high: int) -> int:
    """
    Разбивает массив вокруг опорного элемента (последнего).
    Возвращает финальную позицию опорного элемента.
    """
    pivot = arr[high]
    i = low  # указатель на место для элементов меньше pivot

    for j in range(low, high):
        if arr[j] <= pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1

    # Ставим опорный на своё место
    arr[i], arr[high] = arr[high], arr[i]
    return i