import pytest

from src import get_mask_account, get_mask_card_number


@pytest.mark.parametrize(
    "some_data, expected",
    [
        (1234567843218765, "1234 56** **** 8765"),
        (12345678, "Ошибка. Проверьте правильность введённого номера карты и повторите попытку."),
        ("1234567843218765", "Ошибка, функция принимает только данные типа INT."),
    ],
)
def test_get_mask_card_number(some_data: int | str, expected: str) -> None:
    assert get_mask_card_number(some_data) == expected  # type: ignore


@pytest.mark.parametrize(
    "some_data, expected",
    [
        (12345678432187651234, "**1234"),
        (12345678, "Ошибка. Проверьте правильность введённого номера счёта и повторите попытку."),
        ("12345678432187651234", "Ошибка, функция принимает только данные типа INT."),
    ],
)
def test_get_mask_account(some_data: int | str, expected: str) -> None:
    assert get_mask_account(some_data) == expected  # type: ignore
