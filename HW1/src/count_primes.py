def count_primes(n: int) -> int:
    """
    Подсчитывает количество простых чисел меньше заданного числа N.

    :param n: Целое число, верхняя граница (не включается).
    :return: Количество простых чисел меньше N.
    """
    if n <= 2:
        return 0

    # Создаём решето Эратосфена
    is_prime = [True] * n
    is_prime[0] = is_prime[1] = False

    for i in range(2, int(n ** 0.5) + 1):
        if is_prime[i]:
            # Помечаем все кратные i как непростые
            for j in range(i * i, n, i):
                is_prime[j] = False

    # Подсчитываем количество простых чисел
    return sum(1 for i in range(n) if is_prime[i])