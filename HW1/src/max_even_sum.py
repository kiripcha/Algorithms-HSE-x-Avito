def max_even_sum(arr: list[int]) -> int:
    """
    Находит максимальную сумму элементов массива, которая делится на 2.

    :param arr: Список целых положительных чисел.
    :return: Максимальная сумма, делящаяся на 2, или 0, если такой суммы нет.
    """
    if not arr:
        return 0

    max_sum = 0
    n = len(arr)

    # Перебираем все возможные подмножества, исключая пустое (mask != 0)
    for mask in range(1, 1 << n):  # Начинаем с 1, чтобы исключить пустое подмножество
        current_sum = 0
        for i in range(n):
            if mask & (1 << i):  # Если i-й элемент включён в подмножество
                current_sum += arr[i]
        if current_sum % 2 == 0 and current_sum > max_sum:
            max_sum = current_sum

    return max_sum