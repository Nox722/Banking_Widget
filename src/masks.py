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


def get_mask_card_number(card_number: str) -> str:
    """принимает на вход номер карты и возвращает его маску"""
    mask = ""

    if isinstance(card_number, str):
        if len(card_number) == 16:

            card_logger.info("Маскировка номера карты.")
            for i in range(len(card_number)):

                if 6 <= i <= 11:

                    if i % 4 == 0:
                        mask += " "
                    mask += "*"

                elif i % 4 == 0 and i != 0:
                    mask += " "
                    mask += card_number[i]
                else:
                    mask += card_number[i]

            return mask
        else:
            card_logger.error("Ошибка. Некорректная длина номера карты.")
            return "Ошибка. Проверьте правильность введённого номера карты и повторите попытку."
    else:
        card_logger.error("Ошибка. Некорректный тип данных.")
        return "Ошибка, функция принимает только данные типа STR."


def get_mask_account(account_number: str) -> str:
    """принимает на вход номер счета и возвращает его маску"""

    if isinstance(account_number, str):
        if len(account_number) == 20:
            account_logger.info("Маскировка номера счета.")
            mask = "**" + account_number[-4:]
            return mask
        else:
            account_logger.error("Ошибка. Некорректная длина номера счета.")
            return "Ошибка. Проверьте правильность введённого номера счёта и повторите попытку."
    else:
        account_logger.error("Ошибка. Некорректный тип данных.")
        return "Ошибка, функция принимает только данные типа STR."
