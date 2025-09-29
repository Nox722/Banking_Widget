import functools
import sys
from typing import Any, Callable, Optional


def log(filename: Optional[str] = None) -> Callable:
    def wrapper(func: Callable) -> Callable:
        @functools.wraps(func)
        def inner(*args: Any, **kwargs: Any) -> Any:
            out: Any
            if filename:
                out = open(filename, "a", encoding="utf-8")
            else:
                out = sys.stdout
            print(f"Начало: {func.__name__}", file=out)
            try:
                result = func(*args, **kwargs)
                print(f"Конец: {func.__name__}, результат: {result}", file=out)
                return result
            except Exception as e:
                print(f"Ошибка в: {func.__name__} -> {type(e).__name__}", file=out)
                print(f"Параметры: args={args}, kwargs={kwargs}", file=out)
                raise
            finally:
                if filename:
                    out.close()

        return inner

    return wrapper
