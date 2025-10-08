def two_sum(arr, k):
    '''Находит индексы двух элементов в массиве, сумма которых равна k'''
    seen = {}
    for i, num in enumerate(arr):
        complement = k - num
        if complement in seen:
            return [min(seen[complement], i), max(seen[complement], i)]
        seen[num] = i
    return []