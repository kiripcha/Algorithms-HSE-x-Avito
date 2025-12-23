import pytest
from src.rabin_karp import rabin_karp

@pytest.mark.parametrize(
    "text, pattern, expected",
    [
        ("", "", []),  # Пустой текст и паттерн
        ("", "a", []),  # Пустой текст, непустой паттерн
        ("a", "", []),  # Непустой текст, пустой паттерн
        ("a", "b", []),  # Нет совпадения
        ("a", "a", [0]),  # Одно совпадение
        ("abc", "bc", [1]),  # Совпадение в конце
        ("abc", "ab", [0]),  # Совпадение в начале
        ("aaa", "aa", [0, 1]),  # Множественные перекрывающиеся
        ("abab", "ab", [0, 2]),  # Множественные без перекрытия
        ("abcde", "xyz", []),  # Нет совпадения
        ("a" * 100, "a" * 50, list(range(51))),  # Длинный текст, длинный паттерн, множественные
        ("abcabc", "abc", [0, 3]),  # Повторяющийся
        ("abcaabc", "aabc", [3]),  # С префиксом
        ("hello world", "world", [6]),  # С пробелами
        ("1234567890", "456", [3]),  # Цифры
        ("special!@#", "!@#", [7]),  # Специальные символы
        ("aaaba", "aab", [1]),  # Возможная коллизия, но проверка строки
        ("a" * 1000 + "b", "b", [1000]),  # Длинный текст
        ("abc", "abcd", []),  # Паттерн длиннее текста
    ]
)
def test_rabin_karp(text, pattern, expected):
    assert rabin_karp(text, pattern) == expected

def test_unicode():
    text = "こんにちは世界"
    pattern = "世界"
    assert rabin_karp(text, pattern) == [5]  # Юникод символы

def test_case_sensitive():
    assert rabin_karp("AbC", "bc", [])  # Чувствителен к регистру
    assert rabin_karp("AbC", "bC", [1])

def test_multiple_matches_long():
    text = "ab" * 50
    pattern = "abab"
    expected = [i for i in range(0, 98, 2)]  # Каждые два символа
    assert rabin_karp(text, pattern) == expected

def test_collision_prone():
    # Пример, где хэши могут совпадать, но строки нет (зависит от mod, но проверяем строку)
    text = "aabb"
    pattern = "aaba"  # Предполагаем возможную коллизию, но алгоритм проверяет строку
    assert rabin_karp(text, pattern) == []