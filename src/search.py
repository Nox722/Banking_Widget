import re


def process_bank_search(data: list[dict], search: str = "") -> list[dict]:
    """
    принимает список словарей с данными о банковских операциях и строку поиска,
    а возвращает список словарей, у которых в описании есть данная строка
    """
    try:
        pattern = re.compile(search, re.IGNORECASE)
    except re.error:
        return []
    return [op for op in data if pattern.search(op.get("description", ""))]
