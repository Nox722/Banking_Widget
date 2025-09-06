from .masks import get_mask_account, get_mask_card_number


def mask_account_card(card_or_account_info: str) -> str:
    """принимает на вход тип и номер карты или счета и возвращает его маску"""
    card_or_account = "".join([i for i in card_or_account_info if i.isalpha()])

    list_of_digits = [i for i in card_or_account_info if i.isdigit()]
    number = int("".join(list_of_digits))

    if len(str(number)) > 16:
        return card_or_account + " " + get_mask_account(number)

    return card_or_account + " " + get_mask_card_number(number)


def get_date(date: str) -> str:
    """принимает на вход дату в формате YYYY-MM-DDThh:mm:ss.hhmmss и возвращает строку с датой в формате DD.MM.YYYY"""
    formatted_date = ".".join(date[:10].split("-")[::-1])
    return formatted_date
