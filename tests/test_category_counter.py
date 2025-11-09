from typing import Any

from src import process_bank_operations


def test_process_bank_operations(transactions_list: list[dict[str, Any]]) -> None:
    # считаем операции по заданным категориям
    assert process_bank_operations(transactions_list, ["Перевод организации", "Перевод с карты на карту"]) == {
        "Перевод организации": 2,
        "Перевод с карты на карту": 1,
    }


def test_process_bank_operations_no_categories(transactions_list: list[dict[str, Any]]) -> None:
    # передаем пустой список категорий
    assert process_bank_operations(transactions_list, []) == {}


def test_process_bank_operations_nonexistent_category(transactions_list: list[dict[str, Any]]) -> None:
    # передаем несуществующую категорию
    assert process_bank_operations(transactions_list, ["Перевод организации", "Перевод со счета на карту"]) == {
        "Перевод организации": 2
    }


def test_process_bank_operations_no_transactions() -> None:
    # передаем пустой список транзакций
    assert process_bank_operations([], ["Перевод организации"]) == {}
