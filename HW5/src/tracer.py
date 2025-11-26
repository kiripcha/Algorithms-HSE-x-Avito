import functools
from threading import local
from typing import Any, Callable, TypeVar

F = TypeVar("F", bound=Callable[..., Any])

# у каждого потока своя глубина для каждой функции
_thread_local = local()


def trace(func: F) -> F:
    """
    декоратор для визуализации стека рекурсивных вызовов.
    работает с обычной и взаимной рекурсией.
    """
    func_name = func.__name__

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        depth = getattr(_thread_local, func_name, 0)

        setattr(_thread_local, func_name, depth + 1)

        indent = "  " * depth

        arg_str = ", ".join(repr(a) for a in args)
        kwarg_str = ", ".join(f"{k}={v!r}" for k, v in sorted(kwargs.items()))
        full_args = arg_str
        if kwarg_str:
            full_args += (", " if full_args else "") + kwarg_str

        print(f"{indent}→ {func.__name__}({full_args})")

        result = func(*args, **kwargs)

        print(f"{indent}← {func.__name__}() возвращает {result!r}")

        setattr(_thread_local, func_name, depth)

        return result

    return wrapper