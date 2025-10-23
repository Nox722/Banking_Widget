import json


def get_data_from_json_file(path: str) -> list[dict]:
    """принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях"""

    try:
        with open(path, encoding="utf-8") as f:
            data: list[dict] = json.load(f)
            return data
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        return []
