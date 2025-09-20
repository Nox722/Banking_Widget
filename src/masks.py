def get_mask_card_number(card_number: int) -> str:
    """принимает на вход номер карты и возвращает его маску"""
    mask = ""

    if isinstance(card_number, int):
        if len(str(card_number)) == 16:
            card_number_str = str(card_number)

            for i in range(len(card_number_str)):

                if 6 <= i <= 11:

                    if i % 4 == 0:
                        mask += " "
                    mask += "*"

                elif i % 4 == 0 and i != 0:
                    mask += " "
                    mask += card_number_str[i]
                else:
                    mask += card_number_str[i]

            return mask
        else:
            return "Ошибка. Проверьте правильность введённого номера карты и повторите попытку."
    else:
        return "Ошибка, функция принимает только данные типа INT."


def get_mask_account(account_number: int) -> str:
    """принимает на вход номер счета и возвращает его маску"""

    if isinstance(account_number, int):
        if len(str(account_number)) == 20:
            account_number_str = str(account_number)
            mask = "**" + account_number_str[-4:]
            return mask
        else:
            return "Ошибка. Проверьте правильность введённого номера счёта и повторите попытку."
    else:
        return "Ошибка, функция принимает только данные типа INT."
