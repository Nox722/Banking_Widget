def get_mask_card_number(card_number: int) -> str:
    """принимает на вход номер карты и возвращает его маску"""
    mask = ""
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


def get_mask_account(account_number: int) -> str:
    """принимает на вход номер счета и возвращает его маску"""
    account_number_str = str(account_number)
    mask = "**" + account_number_str[-4:]
    return mask
