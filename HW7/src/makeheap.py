def _sift_down(arr, n, i):
    """
    Просеивание вниз для построения min-heap.
    n — размер кучи (может быть меньше len(arr))
    i — индекс узла, с которого начинаем просеивание
    """
    while True:
        smallest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and arr[left] < arr[smallest]:
            smallest = left
        if right < n and arr[right] < arr[smallest]:
            smallest = right

        if smallest == i:
            break

        arr[i], arr[smallest] = arr[smallest], arr[i]
        i = smallest


def makeheap_n_log_n(arr):
    """
    Построение min-heap за O(N log N).
    Последовательно вставляем элементы в кучу, поддерживая свойство кучи.
    """
    heap = []
    for val in arr:
        heap.append(val)
        # Просеивание вверх нового элемента
        child = len(heap) - 1
        while child > 0:
            parent = (child - 1) // 2
            if heap[child] < heap[parent]:
                heap[child], heap[parent] = heap[parent], heap[child]
                child = parent
            else:
                break
    return heap


def makeheap(arr):
    """
    Построение min-heap за O(N).
    Классический алгоритм heapify: начинаем с последнего родителя и просеиваем вниз.
    """
    heap = arr[:]  # копируем, чтобы не мутировать оригинал
    n = len(heap)
    # Последний родитель: (n-2)//2
    for i in range((n - 2) // 2, -1, -1):
        _sift_down(heap, n, i)
    return heap