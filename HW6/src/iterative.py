import time

def time_decorator(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} execution time: {end - start:.6f} seconds")
        return result
    return wrapper

def iterative_mergesort(arr):
    if len(arr) <= 1:
        return arr[:]
    n = len(arr)
    curr_size = 1
    while curr_size < n:
        left = 0
        while left < n - curr_size:
            mid = min(left + curr_size - 1, n - 1)
            right = min(left + 2 * curr_size - 1, n - 1)
            i, j, k = left, mid + 1, 0
            temp = [0] * (right - left + 1)
            while i <= mid and j <= right:
                if arr[i] <= arr[j]:
                    temp[k] = arr[i]
                    i += 1
                else:
                    temp[k] = arr[j]
                    j += 1
                k += 1
            while i <= mid:
                temp[k] = arr[i]
                i += 1
                k += 1
            while j <= right:
                temp[k] = arr[j]
                j += 1
                k += 1
            for idx in range(len(temp)):
                arr[left + idx] = temp[idx]
            left += 2 * curr_size
        curr_size *= 2
    return arr

def iterative_quicksort(arr):
    if len(arr) <= 1:
        return arr[:]
    stack = []
    stack.append(0)
    stack.append(len(arr) - 1)
    while stack:
        high = stack.pop()
        low = stack.pop()
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        pi = i + 1
        if low < pi - 1:
            stack.append(low)
            stack.append(pi - 1)
        if pi + 1 < high:
            stack.append(pi + 1)
            stack.append(high)
    return arr