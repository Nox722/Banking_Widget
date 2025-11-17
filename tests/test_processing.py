from typing import Any

import pytest

from src import filter_by_state, sort_by_date

# ==============================
# Тесты для функции filter_by_state
# ==============================


def test_filter_default_state(
    list_of_dicts: list[dict[str, Any]], list_of_dicts_state_executed: list[dict[str, Any]]
) -> None:
    # по умолчанию фильтруем по EXECUTED
    assert filter_by_state(list_of_dicts) == list_of_dicts_state_executed


def test_filter_canceled_state(
    list_of_dicts: list[dict[str, Any]], list_of_dicts_state_canceled: list[dict[str, Any]]
) -> None:
    # фильтруем по CANCELED
    assert filter_by_state(list_of_dicts, "CANCELED") == list_of_dicts_state_canceled


def test_filter_unknown_state(list_of_dicts: list[dict[str, Any]]) -> None:
    # фильтр по состоянию, которого нет
    assert filter_by_state(list_of_dicts, "UNKNOWN_STATE") == []


def test_filter_no_key(
    list_of_dicts_no_state: list[dict[str, Any]], list_of_dicts_state_executed: list[dict[str, Any]]
) -> None:
    # передаем список, в котором нет ключа state
    assert filter_by_state(list_of_dicts_no_state) == list_of_dicts_state_executed


def test_filter_empty_list() -> None:
    # передаем пустой список
    assert filter_by_state([]) == []


# ==============================
# Тесты для функции sort_by_date
# ==============================


def test_sort_by_date_descending(
    list_of_dicts: list[dict[str, Any]], list_of_dicts_sorting_by_descending_date: list[dict[str, Any]]
) -> None:
    # сортировка по умолчанию (по убыванию)
    assert sort_by_date(list_of_dicts) == list_of_dicts_sorting_by_descending_date


def test_sort_by_date_increasing(
    list_of_dicts: list[dict[str, Any]], list_of_dicts_sorting_by_increasing_date: list[dict[str, Any]]
) -> None:
    # сортировка по возрастанию
    assert sort_by_date(list_of_dicts, False) == list_of_dicts_sorting_by_increasing_date


def test_sort_by_date_without_date(
    list_of_dicts_without_date: list[dict[str, Any]], list_of_dicts_without_date_sorted: list[dict[str, Any]]
) -> None:
    # сортировка, если в некоторых словарях нет даты
    assert sort_by_date(list_of_dicts_without_date) == list_of_dicts_without_date_sorted


def test_sort_by_unusual_date(list_of_dicts_unexpected_date: list[dict[str, Any]]) -> None:
    # сортировка при необычном формате даты
    with pytest.raises(ValueError) as exc_info:
        sort_by_date(list_of_dicts_unexpected_date)

    assert str(exc_info.value) == "Некорректный формат даты"


def test_sort_by_date_empty_list() -> None:
    # передаём пустой список
    assert sort_by_date([]) == []
