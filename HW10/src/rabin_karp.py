from typing import List

def rabin_karp(text: str, pattern: str) -> List[int]:
    if not pattern:
        return []  # Пустой паттерн не ищем
    n, m = len(text), len(pattern)
    if m > n:
        return []  # Паттерн длиннее текста
    base = 256  # База для хэша (кол-во символов)
    mod = 10**9 + 7  # Большое простое для модуля
    # Хэш паттерна
    hash_p = 0
    for c in pattern:
        hash_p = (hash_p * base + ord(c)) % mod
    # Хэш первого окна текста
    hash_t = 0
    for c in text[:m]:
        hash_t = (hash_t * base + ord(c)) % mod
    # Предвычисленная степень base^{m-1} % mod
    base_pow = pow(base, m - 1, mod)
    results = []
    # Проверка первого окна
    if hash_t == hash_p and text[:m] == pattern:
        results.append(0)
    # Скольжение по тексту
    for i in range(1, n - m + 1):
        # Rolling hash: удалить левый символ, добавить правый
        hash_t = (hash_t - ord(text[i - 1]) * base_pow) % mod
        hash_t = (hash_t * base + ord(text[i + m - 1])) % mod
        hash_t = (hash_t + mod) % mod  # Избежать отрицательного
        if hash_t == hash_p and text[i:i + m] == pattern:
            results.append(i)
    return results