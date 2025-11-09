import json
import logging
import os

root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    filename=os.path.join(root_path, "logs/utils.log"),
    filemode="w",
)

logger = logging.getLogger("utils")


def get_data_from_json_file(path: str) -> list[dict]:
    """принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях"""
    try:
        logger.info("Открытие файла.")
        with open(path, encoding="utf-8") as f:
            logger.info("Чтение JSON-файла.")
            data: list[dict] = json.load(f)
            return data
    except (FileNotFoundError, json.decoder.JSONDecodeError) as ex:
        logger.error(f"Произошла ошибка {ex}.")
        return []
