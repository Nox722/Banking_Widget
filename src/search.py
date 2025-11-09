import re


def process_bank_search(data: list[dict], search: str) -> list[dict]:
    pattern = re.compile(search, re.IGNORECASE)
    return [op for op in data if pattern.search(op.get("description", ""))]
