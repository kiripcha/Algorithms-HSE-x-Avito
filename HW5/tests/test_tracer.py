import pytest
import sys
from io import StringIO

from src.tracer import trace


def capture_output(func, *args, **kwargs):
    old = sys.stdout
    sys.stdout = StringIO()
    try:
        res = func(*args, **kwargs)
        return res, sys.stdout.getvalue()
    finally:
        sys.stdout = old


def lines(output: str):
    """возвращает строки как есть — с ведущими пробелами, без \n в конце"""
    return [line.rstrip("\n") for line in output.splitlines() if line.rstrip()]


# =================================================================


def test_factorial_tracing():
    @trace
    def fact(n: int) -> int:
        return 1 if n == 0 else n * fact(n - 1)

    res, out = capture_output(fact, 4)
    assert res == 24
    L = lines(out)

    expected = [
        "→ fact(4)",
        "  → fact(3)",
        "    → fact(2)",
        "      → fact(1)",
        "        → fact(0)",
        "        ← fact() возвращает 1",
        "      ← fact() возвращает 1",
        "    ← fact() возвращает 2",
        "  ← fact() возвращает 6",
        "← fact() возвращает 24",
    ]
    for e in expected:
        assert e in L


# def test_fibonacci_tracing():
#     @trace
#     def fib(n: int) -> int:
#         if n <= 1:
#             return n
#         return fib(n - 1) + fib(n - 2)

#     res, out = capture_output(fib, 5)
#     assert res == 5
#     L = lines(out)

#     entries = [ln for ln in L if ln.lstrip().startswith("→ fib(")]
#     assert len(entries) == 15

#     # только ведущие пробелы
#     depths = []
#     for ln in L:
#         if ln.startswith("→"):
#             leading_spaces = len(ln) - len(ln.lstrip(" "))
#             depth = leading_spaces // 2
#             depths.append(depth)

#     assert max(depths) == 5, f"максимальная глубина: {max(depths)}, ожидалось 5"


def test_simple_recursive_sum():
    @trace
    def rsum(n: int) -> int:
        if n <= 0:
            return 0
        return n + rsum(n - 1)

    res, out = capture_output(rsum, 3)
    assert res == 6
    L = lines(out)
    assert "→ rsum(3)" in L
    assert "  → rsum(2)" in L
    assert "    → rsum(1)" in L
    assert "      → rsum(0)" in L


# def test_mutual_recursion():
#     @trace
#     def is_even(n: int) -> bool:
#         if n == 0:
#             return True
#         return is_odd(n - 1)

#     @trace
#     def is_odd(n: int) -> bool:
#         if n == 0:
#             return False
#         return is_even(n - 1)

#     res, out = capture_output(is_even, 4)
#     assert res is True
#     L = lines(out)

#     # убираем лишний пробел в начале строк
#     expected = [
#         "→ is_even(4)",
#         "  → is_odd(3)",    
#         "    → is_even(2)",
#         "      → is_odd(1)",
#         "        → is_even(0)",
#         "        ← is_even() возвращает True",
#         "      ← is_odd() возвращает True",
#         "    ← is_even() возвращает False",
#         "  ← is_odd() возвращает False",
#         "← is_even() возвращает True",
#     ]
#     for e in expected:
#         assert e in L, f"не найдена строка: {e!r}\nфактические строки:\n" + "\n".join(L)


def test_kwargs():
    @trace
    def f(x, y=10):
        return x + y

    res, out = capture_output(f, 5, y=20)
    L = lines(out)
    assert L[0] == "→ f(5, y=20)"


def test_no_args():
    @trace
    def hello():
        return "world"

    res, out = capture_output(hello)
    L = lines(out)
    assert L == ["→ hello()", "← hello() возвращает 'world'"]


# def test_deep_recursion():
#     sys.setrecursionlimit(200)

#     @trace
#     def deep(n: int):
#         return "done" if n == 0 else deep(n - 1)

#     res, out = capture_output(deep, 7)
#     L = lines(out)
#     entries = [ln for ln in L if ln.startswith("→")]
#     assert len(entries) == 8
#     depths = [(len(ln) - len(ln.lstrip(" "))) // 2 for ln in entries]
#     assert depths == [0, 1, 2, 3, 4, 5, 6, 7]
#     assert res == "done"