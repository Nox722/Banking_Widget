# BankingWidget
Учебный проект, реализующий набор функций для обработки и маскировки данных банковских карт и счетов, а также для фильтрации и сортировки операций по дате и состоянию.

## Реализованные функции
### - `get_mask_card_number(card_number: int) -> str`  
Принимает на вход номер карты и возвращает его маску.  
**Пример:**  
`get_mask_card_number(1234567890123456) → "1234 56** **** 3456"`

### - `get_mask_account(account_number: int) -> str`
Принимает на вход номер счета и возвращает его маску.  
**Пример:**  
`get_mask_account(40817810099910004312) → "**4312"`

### - `mask_account_card(card_or_account_info: str) -> str`
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
# Вывод:
# [{"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
#  {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"}]
```
### - `sort_by_date(operations: list[dict], order_of_sorting: bool = True) -> list[dict]`
Сортирует список транзакций по дате, по умолчанию — в порядке убывания (от новых к старым).  
**Пример:**  
```
transactions = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"}
]

sorted_transactions = sort_by_date(transactions)
print(sorted_transactions)
# Вывод:
# [
#   {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
#   {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
#   {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
#   {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"}
# ]
```

## Установка и использование
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
from src import (
    get_mask_card_number,
    get_mask_account,
    mask_account_card,
    get_date,
    filter_by_state,
    sort_by_date
)
```
## Лицензия:
Этот проект лицензирован по [лицензии MIT](LICENSE).