import logging
import os

root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    filename=os.path.join(root_path, "logs/masks.log"),
    filemode="w",
)

card_logger = logging.getLogger("get_mask_card_number")
account_logger = logging.getLogger("get_mask_account")


def get_mask_card_number(card_number: int) -> str:
    """принимает на вход номер карты и возвращает его маску"""
    mask = ""

    if isinstance(card_number, int):
        if len(str(card_number)) == 16:
            card_number_str = str(card_number)

            card_logger.info("Маскировка номера карты.")
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
            card_logger.error("Ошибка. Некорректная длина номера карты.")
            return "Ошибка. Проверьте правильность введённого номера карты и повторите попытку."
    else:
        card_logger.error("Ошибка. Некорректный тип данных.")
        return "Ошибка, функция принимает только данные типа INT."


def get_mask_account(account_number: int) -> str:
    """принимает на вход номер счета и возвращает его маску"""

    if isinstance(account_number, int):
        if len(str(account_number)) == 20:
            account_logger.info("Маскировка номера счета.")
            account_number_str = str(account_number)
            mask = "**" + account_number_str[-4:]
            return mask
        else:
            account_logger.error("Ошибка. Некорректная длина номера счета.")
            return "Ошибка. Проверьте правильность введённого номера счёта и повторите попытку."
    else:
        account_logger.error("Ошибка. Некорректный тип данных.")
        return "Ошибка, функция принимает только данные типа INT."


if __name__ == "__main__":
    get_mask_card_number(1234567843218765)
    get_mask_account(12345678432187651234)
