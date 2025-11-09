from collections import Counter


def process_bank_operations(data: list[dict], categories: list) -> dict:
    all_categories = [op.get("description", "") for op in data]
    required_categories = [category for category in all_categories if category in categories]
    return Counter(required_categories)
