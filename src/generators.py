from typing import Any, Iterator


def filter_by_currency(transactions: list[dict[str, Any]], currency: str = "USD") -> Iterator[dict[str, Any]]:
    """Принимает список транзакций и валюту и возвращает итератор транзакций с указанной валютой (по умолчанию USD)"""
    if not isinstance(transactions, list):
        raise TypeError("Ошибка. Ожидаются данные типа list")

    for transaction in transactions:
        try:
            if transaction["operationAmount"]["currency"]["code"] == currency:
                yield transaction
        except KeyError:
            continue


def transaction_descriptions(transactions: list[dict[str, Any]]) -> Iterator[dict[str, Any]]:
    """Принимает на вход список транзакций и возвращает итератор описаний транзакций"""
    for transaction in transactions:
        yield transaction["description"]


def card_number_generator(start: int, stop: int) -> Iterator[str]:
    """Принимает 2 числа - start и stop и возвращает итератор номеров карт в этом диапазоне"""

    if (
        not isinstance(start, int)
        or not isinstance(stop, int)
        or start < 0
        or start > 9999999999999999
        or stop < 0
        or stop > 9999999999999999
    ):
        raise TypeError("Аргументы должны быть целыми числами в диапазоне от 0 до 9999999999999999 включительно")
    if start > stop:
        raise ValueError("Начальное значение не может быть больше конечного")

    for numbers in range(start, stop + 1):
        numbers_str = str(numbers).zfill(16)
        card_number = " ".join([numbers_str[i : i + 4] for i in range(0, len(numbers_str), 4)])
        yield card_number
