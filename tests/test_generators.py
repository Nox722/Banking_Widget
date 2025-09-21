from typing import Any

import pytest

from src import card_number_generator, filter_by_currency, transaction_descriptions

# ==============================
# Тесты для функции filter_by_currency
# ==============================


def test_filter_by_currency_usd(
    transactions_list: list[dict[str, Any]], transactions_list_usd: list[dict[str, Any]]
) -> None:
    # по умолчанию фильтруем по валюте USD
    assert list(filter_by_currency(transactions_list)) == transactions_list_usd


def test_filter_by_currency_eur(transactions_list: list[dict[str, Any]]) -> None:
    # фильтруем по валюте, которой нет в списке (EUR)
    assert list(filter_by_currency(transactions_list, "EUR")) == []


def test_filter_by_currency_empty_list() -> None:
    # передаём пустой список
    assert list(filter_by_currency([])) == []


def test_filter_by_currency_key_error(transactions_list_no_currency: list[dict[str, Any]]) -> None:
    # в переданном списке отсутствует информация о валюте
    assert list(filter_by_currency(transactions_list_no_currency)) == []


def test_filter_by_currency_unexpected_data() -> None:
    # передаём неожиданные данные
    with pytest.raises(TypeError) as exc_info:
        gen = filter_by_currency("surprise")  # type: ignore
        next(gen)

    assert str(exc_info.value) == "Ошибка. Ожидаются данные типа list"


# ==============================
# Тесты для функции transaction_descriptions
# ==============================


def test_transaction_descriptions(transactions_list: list[dict[str, Any]]) -> None:
    # проверка работы функции
    gen = transaction_descriptions(transactions_list)
    assert next(gen) == "Перевод организации"
    assert next(gen) == "Перевод со счета на счет"
    assert next(gen) == "Перевод со счета на счет"
    assert next(gen) == "Перевод с карты на карту"
    assert next(gen) == "Перевод организации"


def test_transaction_descriptions_empty_list() -> None:
    # передаём пустой список
    assert list(transaction_descriptions([])) == []


# ==============================
# Тесты для функции card_number_generator
# ==============================


@pytest.mark.parametrize(
    "a, b, expected_results",
    [
        (
            1,
            10,
            [
                "0000 0000 0000 0001",
                "0000 0000 0000 0002",
                "0000 0000 0000 0003",
            ],
        ),
        (
            8,
            10,
            [
                "0000 0000 0000 0008",
                "0000 0000 0000 0009",
                "0000 0000 0000 0010",
            ],
        ),
    ],
)
def test_card_number_generator(a: int, b: int, expected_results: str) -> None:
    gen = card_number_generator(a, b)
    for expected in expected_results:
        assert next(gen) == expected


@pytest.mark.parametrize(
    "a, b, expected_result",
    [
        (
            -2,
            5,
            "Аргументы должны быть целыми числами в диапазоне от 0 до 9999999999999999 включительно",
        ),
        (
            9999999999999998,
            10000000000000000,
            "Аргументы должны быть целыми числами в диапазоне от 0 до 9999999999999999 включительно",
        ),
    ],
)
def test_card_number_generator_unexpected_data(a: int, b: int, expected_result: str) -> None:
    # тестирование ошибок
    with pytest.raises(TypeError) as exc_info:
        gen = card_number_generator(a, b)
        next(gen)

    assert str(exc_info.value) == expected_result


def test_card_number_generator_arg_error() -> None:
    # Если первый аргумент больше второго
    with pytest.raises(ValueError) as exc_info:
        gen = card_number_generator(5, 2)
        next(gen)

    assert str(exc_info.value) == "Начальное значение не может быть больше конечного"
