from collections import Counter


def process_bank_operations(data: list[dict], categories: list) -> dict:
    """
    принимает список словарей с данными о банковских операциях и список категорий операций,
    а возвращает словарь, в котором ключи — это названия категорий,
    а значения — это количество операций в каждой категории
    """
    all_categories = [op.get("description", "") for op in data]
    required_categories = [category for category in all_categories if category in categories]
    return Counter(required_categories)
