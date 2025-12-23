import heapq
from typing import List

# ==================== 1. Реализация без heapq (своя min-heap) ====================

class MinHeap:
    def __init__(self):
        self.heap = []

    def push(self, val: int):
        self.heap.append(val)
        self._sift_up(len(self.heap) - 1)

    def pop(self) -> int:
        if len(self.heap) == 1:
            return self.heap.pop()
        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._sift_down(0)
        return root

    def peek(self) -> int:
        return self.heap[0]

    def size(self) -> int:
        return len(self.heap)

    def _sift_up(self, i: int):
        while i > 0:
            parent = (i - 1) // 2
            if self.heap[i] < self.heap[parent]:
                self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
                i = parent
            else:
                break

    def _sift_down(self, i: int):
        n = len(self.heap)
        while True:
            smallest = i
            left = 2 * i + 1
            right = 2 * i + 2
            if left < n and self.heap[left] < self.heap[smallest]:
                smallest = left
            if right < n and self.heap[right] < self.heap[smallest]:
                smallest = right
            if smallest == i:
                break
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            i = smallest


def kth_largest_manual(nums: List[int], k: int) -> int:
    """
    Находит k-ый по величине элемент, используя собственную реализацию min-heap.
    Поддерживаем кучу размера k: в ней всегда находятся k наибольших элементов.
    Корень — наименьший из них, то есть k-ый по величине.
    """
    if not nums or k < 1 or k > len(nums):
        raise ValueError("Invalid input")

    heap = MinHeap()
    for num in nums:
        heap.push(num)
        if heap.size() > k:
            heap.pop()

    return heap.peek()


# ==================== 2. Реализация с использованием heapq ====================

def kth_largest_heapq(nums: List[int], k: int) -> int:
    """
    То же самое, но с использованием стандартной библиотеки heapq.
    heapq — min-heap, поэтому логика идентична.
    """
    if not nums or k < 1 or k > len(nums):
        raise ValueError("Invalid input")

    heap = []
    for num in nums:
        heapq.heappush(heap, num)
        if len(heap) > k:
            heapq.heappop(heap)

    return heap[0]