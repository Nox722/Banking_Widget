from typing import Any

from src import process_bank_search


def test_process_bank_search(
    transactions_list: list[dict[str, Any]], transactions_list_acc_to_acc: list[dict[str, Any]]
) -> None:
    # ищем банковские операции по описанию
    assert process_bank_search(transactions_list, "Перевод со счета на счет") == transactions_list_acc_to_acc


def test_process_bank_search_empty_search(transactions_list: list[dict[str, Any]]) -> None:
    # поиск по умолчанию (search - пустая строка)
    assert process_bank_search(transactions_list) == transactions_list


def test_process_bank_search_invalid_regular_expression(transactions_list: list[dict[str, Any]]) -> None:
    # передаем неправильное регулярное выражение
    assert process_bank_search(transactions_list, "([unclosed") == []


def test_process_bank_search_no_transactions() -> None:
    # передаем пустой список
    assert process_bank_search([]) == []
