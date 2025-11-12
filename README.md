# BankingWidget
Учебный проект, реализующий набор функций для обработки и маскировки данных банковских карт и счетов, а также для фильтрации и сортировки операций по дате и состоянию.

## I Реализованные функции
### - `get_mask_card_number(card_number: int) -> str`  
Принимает на вход номер карты и возвращает его маску.  

**Пример:**  
`get_mask_card_number(1234567890123456) → "1234 56** **** 3456"`

### - `get_mask_account(account_number: int) -> str`
Принимает на вход номер счета и возвращает его маску.  

**Пример:**  
`get_mask_account(40817810099910004312) → "**4312"`

### - `mask_account_card(card_or_account_info: str | int) -> str`
Принимает на вход тип и номер карты или счета и возвращает его маску.  
Определяет, что маскировать — карту или счет — по длине номера.  

**Пример:**  
`mask_account_card("Visa Platinum 7000792289606361") → "VisaPlatinum 7000 79** **** 6361"`   
`mask_account_card("Счет 73654108430135874305") → "Счет **4305"`

### - `get_date(date: str) -> str`
Принимает на вход дату в формате YYYY-MM-DDThh:mm:ss.hhmmss и возвращает строку с датой в формате DD.MM.YYYY.  

**Пример:**  
`get_date("2024-03-11T02:26:18.671407") → "11.03.2024"`

### - `filter_by_state(operations: list[dict], desired_state: str = "EXECUTED") -> list[dict]`
Фильтрует список транзакций по заданному состоянию. Состояние по умолчанию — "EXECUTED".  

**Пример:**  
```
transactions = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"}
]

executed_transactions = filter_by_state(transactions)
print(executed_transactions)

>>> [
      {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
      {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"}
    ]
```


### - `sort_by_date(operations: list[dict], order_of_sorting: bool = True) -> list[dict]`
Сортирует список транзакций по дате, по умолчанию — в порядке убывания (от новых к старым).  

**Пример:**  
```
sorted_transactions = sort_by_date(transactions)
# в качестве аргумента функции использован список из предыдущего примера

print(sorted_transactions)

>>> [
      {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
      {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
      {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
      {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"}
    ]
```

### - `filter_by_currency(transactions: list[dict[str, Any]], currency: str = "USD") -> Iterator[dict[str, Any]]`
Принимает список транзакций и валюту и возвращает итератор транзакций с указанной валютой (по умолчанию USD).  

**Пример:**  
```
transactions = [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160",
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229",
        },
    ]

usd_transactions = filter_by_currency(transactions, "USD")
for _ in range(2):
    print(next(usd_transactions))

>>> {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
    }
    {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229",
    }
```

### - `transaction_descriptions(transactions: list[dict[str, Any]]) -> Iterator[dict[str, Any]]`
Принимает на вход список транзакций и возвращает итератор описаний транзакций.  

**Пример:**  
```
descriptions = transaction_descriptions(transactions)  
# в качестве аргумента функции использован список из предыдущего примера

for _ in range(3):
    print(next(descriptions))
    
>>> Перевод организации
    Перевод со счета на счет
    Перевод с карты на карту
```

### - `card_number_generator(start: int, stop: int) -> Iterator[str]`
Принимает 2 числа - start и stop и возвращает итератор номеров карт в этом диапазоне.  

**Пример:**  
```
for card_number in card_number_generator(1, 5):
    print(card_number)

>>> 0000 0000 0000 0001
    0000 0000 0000 0002
    0000 0000 0000 0003
    0000 0000 0000 0004
    0000 0000 0000 0005
```
### - `log(filename: Optional[str] = None) -> Callable`
Декоратор для логирования вызовов функции.   
Записывает в файл (или в стандартный вывод, если filename=None) информацию о начале и конце выполнения функции, а также результат. В случае исключения логирует его тип и параметры вызова.  

**Пример:**  
```
@log(filename=None)  # Логирование в консоль
def greet(name: str) -> str:
    return f"Привет, {name}!"

@log(filename="app.log")  # Логирование в файл app.log
def divide(a: float, b: float) -> float:
    return a / b

print(greet("Мир"))

divide(10, 0)
```
### - `get_data_from_json_file(path: str) -> list[dict]`
Принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях.  

**Пример:**
```
# Путь к вашему JSON-файлу с данными о транзакциях
file_path = "transactions.json"

# Получение данных из файла
transactions = get_data_from_json_file(file_path)
```
### - `get_transaction_amount_in_rubles(transaction: dict) -> float`
Принимает на вход транзакцию и возвращает сумму транзакции в рублях.  

**Пример:**
```
transaction = {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    }
    
get_transaction_amount_in_rubles(transaction) -> 799286.34  # сумма в рублях по текущему курсу
```
### - `get_data_from_csv_file(path: str) -> list[dict]`
Принимает на вход путь до csv-файла и возвращает список словарей с данными о финансовых транзакциях.  

**Пример:**
```
# Путь к вашему csv-файлу с данными о транзакциях
file_path = "transactions.csv"

# Получение данных из файла
transactions = get_data_from_csv_file(file_path)
```
### - `get_data_from_excel_file(path: str) -> list[dict]`
Принимает на вход путь до excel-файла и возвращает список словарей с данными о финансовых транзакциях.  

**Пример:**
```
# Путь к вашему excel-файлу с данными о транзакциях
file_path = "transactions.xlsx"

# Получение данных из файла
transactions = get_data_from_excel_file(file_path)
```
### - `process_bank_search(data: list[dict], search: str = "") -> list[dict]`
Принимает список словарей с данными о банковских операциях и строку поиска, а возвращает список словарей, у которых в описании есть данная строка.

**Пример:**
```
filter = "слова для фильтрации"

transactions = process_bank_search(list_of_dicts, filter)
```
### - `process_bank_operations(data: list[dict], categories: list) -> dict`
Принимает список словарей с данными о банковских операциях и список категорий операций,
а возвращает словарь, в котором ключи — это названия категорий,
а значения — это количество операций в каждой категории

**Пример:**
```
categories_list = ["Открытие вклада", "Перевод организации"]

result_dict = process_bank_search(list_of_dicts, categories_list)
```

## II Установка и использование
### Клонирование репозитория
Сначала склонируйте репозиторий проекта к себе на компьютер:

```
git clone https://github.com/ваш_пользователь/Banking_Widget.git
cd Banking_Widget
```
Замените https://github.com/ваш_пользователь/Banking_Widget.git на реальный URL вашего репозитория.

### Установка (опционально)
Если вы планируете использовать проект как пакет, можно установить его в виртуальное окружение:   
1. Создайте и активируйте виртуальное окружение:
```
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/macOS
source venv/bin/activate
```
2. Установите проект:
```
pip install .
```

### Использование
Импортируйте необходимые функции из пакета src в вашем Python-скрипте:
```
from src import <название функции>
```
Используйте переменные окружения из файла .env для сокрытия чувствительных данных. Шаблон файла - .env.example.
Запустите функцию main в корне проекта.

## III Тестирование
Для проекта написаны юнит-тесты ко всем функциям, что обеспечивает проверку корректности работы и упрощает дальнейшее сопровождение.

Как запустить тесты:  
Убедитесь, что вы находитесь в корне проекта.  
(Опционально) Активируйте виртуальное окружение, если используете его.  
Запустите тесты с помощью pytest:
```
pytest
```
Если pytest не установлен, его можно установить командой:
```
pip install pytest
```
Результаты тестирования помогут убедиться, что все функции работают корректно и изменения не нарушили существующий функционал.

## IV Лицензия:
Этот проект лицензирован по [лицензии MIT](LICENSE).