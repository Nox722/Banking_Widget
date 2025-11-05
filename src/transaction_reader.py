import csv
import os


root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def get_data_from_csv_file(path: str) -> list[dict]:
    """принимает на вход путь до csv-файла и возвращает список словарей с данными о финансовых транзакциях"""
    try:
        with open(path, encoding="utf-8") as f:
            reader = csv.DictReader(f, delimiter=";")
            data = [row for row in reader]
    except FileNotFoundError:
        return []

    return data


def get_data_from_excel_file(path: str) -> list[dict]:
    pass


if __name__ == "__main__":
    file_path = os.path.join(root_path, "data", "transactions.csv")
    data = get_data_from_csv_file(file_path)
    print(data[4:5])