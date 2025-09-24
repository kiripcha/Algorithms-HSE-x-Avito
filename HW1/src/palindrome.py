def is_palindrome(n: int) -> bool:
    """
    Проверяет, является ли положительное целое число палиндромом без использования строк.
    
    :param n: Положительное целое число для проверки.
    :return: True, если число является палиндромом, иначе False.
    """
    if n <= 0:
        return False  # Отрицательные числа и -0 не считаются палиндромами
    
    original = n
    reversed_num = 0
    
    while n > 0:
        digit = n % 10
        reversed_num = reversed_num * 10 + digit
        n = n // 10
    
    return original == reversed_num