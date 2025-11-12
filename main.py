import os

from src.processing import filter_by_state, sort_by_date
from src.search import process_bank_search
from src.transaction_reader import get_data_from_csv_file, get_data_from_excel_file
from src.utils import get_data_from_json_file
from src.widget import get_date, mask_account_card


def main() -> None:
    """
    Основная функция программы обработки банковских транзакций.

    Выполняет последовательность следующих действий:
    - Выбор и загрузка данных из JSON, CSV или XLSX файла.
    - Фильтрация данных по статусу транзакций.
    - Добавление опции сортировки по дате.
    - Фильтрация по валюте (только рубли).
    - Поиск по слову в описании транзакции.
    - Вывод итогового списка с отформатированной информацией.
    """
    # Путь к файлам данных
    data_path_json = os.path.join(os.path.dirname(__file__), "data", "operations.json")
    data_path_csv = os.path.join(os.path.dirname(__file__), "data", "transactions.csv")
    data_path_xlsx = os.path.join(os.path.dirname(__file__), "data", "transactions_excel.xlsx")

    # Изначально список транзакций пустой
    ops_list = []

    # Объявляем переменные для последующего выбора пользователем
    user_file_selection = ""
    user_state_selection = ""
    user_sort_by_date_selection = ""
    user_order_selection = ""
    user_currency_selection = ""
    user_filter_selection = ""

    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")

    # Блок выбора файла-источника данных
    while user_file_selection not in ["1", "2", "3"]:
        print("Выберите необходимый пункт меню:")
        print(
            "1. Получить информацию о транзакциях из JSON-файла\n"
            "2. Получить информацию о транзакциях из CSV-файла\n"
            "3. Получить информацию о транзакциях из XLSX-файла"
        )
        user_file_selection = input("Введите номер опции: ").strip()

        # Загрузка данных в зависимости от выбранного формата
        if user_file_selection == "1":
            print("Для обработки выбран JSON-файл.")
            ops_list = get_data_from_json_file(data_path_json)
        elif user_file_selection == "2":
            print("Для обработки выбран CSV-файл.")
            ops_list = get_data_from_csv_file(data_path_csv)
        elif user_file_selection == "3":
            print("Для обработки выбран XLSX-файл.")
            ops_list = get_data_from_excel_file(data_path_xlsx)
        else:
            print(f"Опция '{user_file_selection}' не существует.")

    # Фильтрация по статусу операции
    while user_state_selection not in ["executed", "canceled", "pending"]:
        print(
            "Введите статус, по которому необходимо выполнить фильтрацию. "
            "Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING"
        )
        user_state_selection = input().lower().strip()

        if user_state_selection not in ["executed", "canceled", "pending"]:
            print(f"Статус операции '{user_state_selection}' недоступен.")

    # Фильтр транзакций по выбранному статусу
    ops_list = filter_by_state(ops_list, user_state_selection.upper())

    # Сортировка по дате
    while user_sort_by_date_selection not in ["да", "нет"]:
        print("Отсортировать операции по дате? Да/Нет")
        user_sort_by_date_selection = input().lower().strip()

        if user_sort_by_date_selection == "да":
            # Внутренний выбор порядка сортировки
            while user_order_selection not in ["по возрастанию", "по убыванию"]:
                print("Отсортировать по возрастанию или по убыванию?")
                user_order_selection = input().lower().strip()

                if user_order_selection == "по возрастанию":
                    ops_list = sort_by_date(ops_list, False)
                elif user_order_selection == "по убыванию":
                    ops_list = sort_by_date(ops_list)

    # Фильтрация транзакций по валюте (только RUB)
    while user_currency_selection not in ["да", "нет"]:
        print("Выводить только рублевые транзакции? Да/Нет")
        user_currency_selection = input().lower().strip()

        if user_currency_selection == "да":
            # Условие для фильтрации по валюте зависит от типа файла
            if user_file_selection == "1":
                ops_list = [op for op in ops_list if op["operationAmount"]["currency"]["code"] == "RUB"]
            elif user_file_selection in ["2", "3"]:
                ops_list = [op for op in ops_list if op["currency_code"] == "RUB"]

    # Фильтр по слову в описании транзакции
    while user_filter_selection not in ["да", "нет"]:
        print("Отфильтровать список транзакций по определенному слову в описании? Да/Нет")
        user_filter_selection = input().lower().strip()

        if user_filter_selection == "да":
            filter_word = input("Введите слово для фильтрации: ").lower().strip()
            ops_list = process_bank_search(ops_list, filter_word)

    # Вывод итогового набора транзакций
    if ops_list != []:
        print("Распечатываю итоговый список транзакций...")
        print(f"Всего банковских операций в выборке: {len(ops_list)}\n")
        for op in ops_list:
            date = get_date(op["date"])
            from_ = mask_account_card(op.get("from"))  # type: ignore
            to = mask_account_card(op["to"])

            # Формат вывода в зависимости от наличия "from"
            if op.get("from"):
                if user_file_selection == "1":
                    print(
                        f"{date} {op["description"]}\n"
                        f"{from_} -> {to}\n"
                        f"Сумма: {op["operationAmount"]['amount']} {op["operationAmount"]["currency"]["name"]}\n"
                    )
                elif user_file_selection in ["2", "3"]:
                    print(
                        f"{date} {op["description"]}\n"
                        f"{from_} -> {to}\n"
                        f"Сумма: {op['amount']} {op["currency_name"]}\n"
                    )
            else:
                # Если "from" отсутствует
                if user_file_selection == "1":
                    print(
                        f"{date} {op["description"]}\n"
                        f"{to}\n"
                        f"Сумма: {op["operationAmount"]['amount']} {op["operationAmount"]["currency"]["name"]}\n"
                    )
                elif user_file_selection in ["2", "3"]:
                    print(f"{date} {op["description"]}\n" f"{to}\n" f"Сумма: {op['amount']} {op["currency_name"]}\n")

    else:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")


if __name__ == "__main__":
    main()
