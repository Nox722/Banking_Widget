from datetime import datetime

from src import get_mask_account, get_mask_card_number


def mask_account_card(card_or_account_info: str) -> str:
    """принимает на вход тип и номер карты или счета и возвращает его маску"""

    card_or_account = "".join([i for i in card_or_account_info if i.isalpha()])

    list_of_digits = [i for i in card_or_account_info if i.isdigit()]
    digits_str = "".join(list_of_digits)

    if not digits_str:
        return "Ошибка. Пожалуйста, введите номер карты или счёта."

    number = digits_str

    if len(number) == 20:
        if card_or_account.lower() == "":
            return get_mask_account(number)
        return card_or_account + " " + get_mask_account(number)
    elif len(number) == 16:
        if card_or_account.lower() == "":
            return get_mask_card_number(number)
        return card_or_account + " " + get_mask_card_number(number)
    else:
        return "Ошибка. Проверьте правильность введённых данных."


def get_date(date_str: str) -> str:
    """принимает на вход дату в формате YYYY-MM-DDThh:mm:ss.hhmmss и возвращает строку с датой в формате DD.MM.YYYY"""
    try:
        dt = datetime.fromisoformat(date_str)
        return dt.strftime("%d.%m.%Y")
    except ValueError:
        return "Ошибка. Некорректный формат даты."


result = mask_account_card("Visa 0264849140954307")
print(result)
