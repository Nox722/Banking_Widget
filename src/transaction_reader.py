import csv
import os

import pandas as pd

root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def get_data_from_csv_file(path: str) -> list[dict]:
    """принимает на вход путь до csv-файла и возвращает список словарей с данными о финансовых транзакциях"""
    try:
        with open(path, encoding="utf-8") as f:
            reader = csv.DictReader(f, delimiter=";")
            csv_data = [row for row in reader]
    except FileNotFoundError:
        print("Файл не найден. Проверьте указанный путь")
        return []
    except Exception as e:
        print(f"Ошибка при чтении файла: {e}")
        return []
    return csv_data


def get_data_from_excel_file(path: str) -> list[dict]:
    """принимает на вход путь до excel-файла и возвращает список словарей с данными о финансовых транзакциях"""
    excel_data_list: list[dict] = []
    try:
        excel_data = pd.read_excel(path, dtype=str)
        excel_data.fillna("", inplace=True)
        excel_data_list = excel_data.to_dict(orient="records")
    except FileNotFoundError:
        print("Файл не найден. Проверьте указанный путь")
        return []
    except Exception as e:
        print(f"Ошибка при чтении файла: {e}")
        return []
    return excel_data_list


if __name__ == "__main__":
    file_path_csv = os.path.join(root_path, "data", "transactions.csv")
    csv_data = get_data_from_csv_file(file_path_csv)
    print(csv_data[4:5])

    file_path_xlsx = os.path.join(root_path, "data", "transactions_excel.xlsx")
    excel_data = get_data_from_excel_file(file_path_xlsx)
    print(excel_data[4:5])

    print(csv_data == excel_data)
