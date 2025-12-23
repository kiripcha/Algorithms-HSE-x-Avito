import pytest
from src.knuth_morris_pratt import kmp_search

@pytest.mark.parametrize(
    "text, pattern, expected",
    [
        ("", "", []),                    # Пустой текст и паттерн
        ("", "a", []),                   # Пустой текст, непустой паттерн
        ("abc", "", []),                 # Непустой текст, пустой паттерн
        ("a", "b", []),                  # Нет совпадения
        ("a", "a", [0]),                 # Одно совпадение
        ("abc", "bc", [1]),              # Совпадение в середине
        ("abc", "ab", [0]),              # Совпадение в начале
        ("aaa", "aa", [0, 1]),           # Перекрывающиеся вхождения
        ("abab", "ab", [0, 2]),          # Множественные без перекрытия
        ("abcabc", "abc", [0, 3]),       # Повторяющийся паттерн
        ("abcaabc", "aabc", [3]),        # Частичное совпадение префикса
        ("abcd", "xyz", []),             # Нет совпадения
        ("hello world", "world", [6]),   # Пробелы
        ("1234567890", "456", [3]),      # Цифры
        ("!@#$%^&*", "^&*", [5]),        # Специальные символы
        ("aaaaaaa", "aaa", [0,1,2,3,4]), # Много перекрывающихся
        ("abcabcd", "abcd", [3]),        # Длинное вхождение
        ("abc", "abcd", []),             # Паттерн длиннее текста
        ("ababa", "aba", [0, 2]),        # Классический пример с частичным совпадением
        ("a" * 100, "a" * 50, list(range(51))),  # Длинный текст и паттерн
        ("abcdabc", "abcdabc", [0]),     # Полное совпадение с текстом
    ]
)
def test_kmp_basic(text, pattern, expected):
    assert kmp_search(text, pattern) == expected

def test_unicode():
    text = "привет мир привет"
    pattern = "привет"
    assert kmp_search(text, pattern) == [0, 11]

def test_case_sensitive():
    assert kmp_search("AbCaBc", "abc", []) == []
    assert kmp_search("AbCaBc", "aBc", []) == [2]

def test_complex_overlap():
    text = "abababababa"
    pattern = "abababa"
    assert kmp_search(text, pattern) == [0, 2, 4]  # Перекрытия через 2 символа

def test_periodic_pattern():
    text = "abcabcabcabc"
    pattern = "abcabc"
    assert kmp_search(text, pattern) == [0, 3, 6]

def test_long_text_short_pattern():
    text = "a" * 1000 + "b"
    pattern = "b"
    assert kmp_search(text, pattern) == [1000]

def test_all_same_characters():
    text = "aaaaaaaaaa"
    pattern = "aaaa"
    expected = list(range(7))  # 0 до 6 включительно
    assert kmp_search(text, pattern) == expected

def test_no_overlap_possible():
    text = "abcdef"
    pattern = "cdf"
    assert kmp_search(text, pattern) == [2]