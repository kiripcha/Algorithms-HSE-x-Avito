import pytest
from src.lcs import longest_common_subsequence

@pytest.mark.parametrize(
    "s1, s2, expected",
    [
        ("", "", 0),                          # Обе строки пустые
        ("", "abc", 0),                       # Первая пустая
        ("abc", "", 0),                       # Вторая пустая
        ("a", "a", 1),                        # Одинаковые одиночные символы
        ("a", "b", 0),                        # Разные одиночные символы
        ("abc", "abc", 3),                    # Полностью одинаковые
        ("abc", "def", 0),                    # Нет общих символов
        ("AGGTAB", "GXTXAYB", 4),             # Классический пример из условия
        ("ABCDGH", "AEDFHR", 3),              # Пример с LCS = "ADH"
        ("ABC", "AC", 2),                     # Вложенная подпоследовательность
        ("ABBA", "BAAB", 3),                  # Симметричные строки
        ("abcd", "acbd", 3),                  # Перестановка символов
        ("aaaa", "aaa", 3),                   # Повторяющиеся символы
        ("abcabc", "abca", 4),                # Длиннее в первой
        ("a" * 50, "a" * 30, 30),             # Длинные одинаковые последовательности
        ("abcde", "ace", 3),                  # Каждый второй символ
        ("xmjyauz", "mzjawxu", 4),            # Сложный случай
        ("abcdef", "fedcba", 1),              # Обратный порядок
        ("pqr", "pqrspqr", 3),                # Вложено несколько раз
        ("hello", "world", 2),                # "lo" или "l" и "o"
        ("python", "pythons", 6),             # Почти одинаковые
        ("абвгд", "вгд", 3),                  # Юникод (кириллица)
        ("!@#$%", "!@#", 3),                  # Специальные символы
    ]
)
def test_lcs_length(s1, s2, expected):
    assert longest_common_subsequence(s1, s2) == expected

def test_large_strings():
    s1 = "a" * 500 + "b" * 500
    s2 = "b" * 500 + "a" * 500
    assert longest_common_subsequence(s1, s2) == 500  # Только все 'a' или все 'b'

def test_all_identical():
    s1 = "abcdef"
    s2 = "abcdef" * 10
    assert longest_common_subsequence(s1, s2) == 6

def test_no_common():
    s1 = "abc123"
    s2 = "def456"
    assert longest_common_subsequence(s1, s2) == 0

def test_single_common_in_middle():
    s1 = "xyzaklm"
    s2 = "pqrast"
    assert longest_common_subsequence(s1, s2) == 1  # только 'a'

def test_case_sensitivity():
    assert longest_common_subsequence("ABC", "abc") == 0  # Чувствителен к регистру
    assert longest_common_subsequence("AbC", "abc") == 1  # Только 'b' или 'c'

def test_repeated_chars_max_use():
    s1 = "aaab"
    s2 = "aaaaac"
    assert longest_common_subsequence(s1, s2) == 4  # Все 'a' из s2 и три из s1 + 'b'? Нет, только 'a': max 4

def test_alternating():
    s1 = "abababab"
    s2 = "babababa"
    assert longest_common_subsequence(s1, s2) == 8  # Вся строка кроме одного символа