import os

import pytest

from src import log


# Тест на успешное выполнение функции с выводом в консоль (filename=None)
def test_log_stdout_success(capsys: pytest.CaptureFixture) -> None:
    @log()
    def add(a: int, b: int) -> int:
        return a + b

    result = add(2, 3)
    captured = capsys.readouterr()

    assert result == 5
    assert "Начало: add" in captured.out
    assert "Конец: add, результат: 5" in captured.out


# Тест на обработку исключения с выводом в консоль
def test_log_stdout_exception(capsys: pytest.CaptureFixture) -> None:
    @log()
    def fail_func() -> None:
        raise ValueError("Ошибка!")

    with pytest.raises(ValueError):
        fail_func()

    captured = capsys.readouterr()
    assert "Начало: fail_func" in captured.out
    assert "Ошибка в: fail_func -> ValueError" in captured.out
    assert "Параметры: args=(), kwargs={}" in captured.out


# Тест записи в файл: успешное выполнение функции + проверка содержимого файла
@pytest.mark.parametrize("filename", ["test_log.txt"])
def test_log_file_success(filename: str) -> None:
    try:

        @log(filename)
        def multiply(a: int, b: int) -> int:
            return a * b

        result = multiply(4, 5)

        assert result == 20

        with open(filename, "r", encoding="utf-8") as f:
            content = f.read()

        assert "Начало: multiply" in content
        assert "Конец: multiply, результат: 20" in content
    finally:
        if os.path.exists(filename):
            os.remove(filename)


# Тест записи в файл: проверка обработки исключения и логирования ошибок
@pytest.mark.parametrize("filename", ["test_log_exception.txt"])
def test_log_file_exception(filename: str) -> None:
    try:

        @log(filename)
        def division(x: float, y: float) -> float:
            return x / y

        with pytest.raises(ZeroDivisionError):
            division(5, 0)

        with open(filename, "r", encoding="utf-8") as f:
            content = f.read()

        assert "Начало: division" in content
        assert "Ошибка в: division -> ZeroDivisionError" in content
        assert "Параметры: args=(5, 0), kwargs={}" in content
    finally:
        if os.path.exists(filename):
            os.remove(filename)
