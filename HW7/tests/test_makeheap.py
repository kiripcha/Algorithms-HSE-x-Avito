# tests/test_heap.py
import pytest
import time
import random
from src.makeheap import makeheap_n_log_n, makeheap

def _is_min_heap(arr):
    """Проверка, является ли массив min-heap"""
    n = len(arr)
    for i in range(n):
        left = 2 * i + 1
        right = 2 * i + 2
        if left < n and arr[left] < arr[i]:
            return False
        if right < n and arr[right] < arr[i]:
            return False
    return True

@pytest.mark.parametrize("func", [makeheap_n_log_n, makeheap])
@pytest.mark.parametrize(
    "input_arr",
    [
        [],                                      # пустой
        [1],                                     # один элемент
        [1, 2],                                  # два элемента
        [2, 1],                                  # два в обратном порядке
        [5, 3, 8, 1, 4, 9, 2],                    # случайный
        [1, 1, 1, 1],                            # все одинаковые
        [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],          # убывающий
        list(range(1, 21)),                      # возрастающий
        [-5, -1, -10, -3, -7],                   # отрицательные
        [0, 0, 0, 0, 0],                         # нули
        [100] * 1000,                            # большой с дубликатами
    ]
)
def test_heap_correctness(func, input_arr):
    result = func(input_arr[:])  # копия, т.к. функции могут мутировать
    assert _is_min_heap(result)
    assert sorted(result) == sorted(input_arr)  # те же элементы


def test_large_random_arrays():
    for n in [1000, 10000]:
        arr = [random.randint(-10000, 10000) for _ in range(n)]
        assert _is_min_heap(makeheap(arr[:]))
        assert _is_min_heap(makeheap_n_log_n(arr[:]))


def test_timing_comparison():
    sizes = [1000, 5000, 10000, 20000]
    print("\nСравнение времени выполнения (в секундах):")
    print("N\t\tO(N log N)\tO(N)\t\tКоэффициент")
    
    for n in sizes:
        arr = [random.randint(0, 1000000) for _ in range(n)]
        
        start = time.time()
        makeheap_n_log_n(arr[:])
        t1 = time.time() - start
        
        start = time.time()
        makeheap(arr[:])
        t2 = time.time() - start
        
        ratio = t1 / t2 if t2 > 0 else float('inf')
        print(f"{n}\t\t{t1:.4f}\t\t{t2:.4f}\t\t{ratio:.2f}x")