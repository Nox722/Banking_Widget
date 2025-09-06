def filter_by_state(operations: list[dict], desired_state: str = "EXECUTED") -> list[dict]:
    """
    принимает список словарей и опционально значение для ключа state и возвращает новый список словарей,
    содержащий только те словари, у которых ключ state соответствует указанному значению
    """
    new_operations_list = [i for i in operations if i['state'] == desired_state]

    return new_operations_list


def sort_by_date(operations: list[dict], order_of_sorting: bool = True) -> list[dict]:
    """
    принимает список словарей и необязательный параметр, задающий порядок сортировки
    и возвращает новый список, отсортированный по дате
    """
    new_operations_list = sorted(operations, key=lambda x: x['date'], reverse=order_of_sorting)

    return new_operations_list
