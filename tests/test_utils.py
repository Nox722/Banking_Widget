import os

import pytest

from src import get_data_from_json_file

current_dir = os.path.dirname(os.path.abspath(__file__))

file_path = os.path.join(current_dir, "data", "test_operations.json")
empty_file_path = os.path.join(current_dir, "data", "test_empty.json")
wrong_file_path = os.path.join(current_dir, "src", "operations.json")
wrong_json_path = os.path.join(current_dir, "data", "test_wrong.json")


@pytest.mark.parametrize(
    "path, expected",
    [
        (
            file_path,
            [
                {
                    "id": 441945886,
                    "state": "EXECUTED",
                    "date": "2019-08-26T10:50:58.294041",
                    "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
                    "description": "Перевод организации",
                    "from": "Maestro 1596837868705199",
                    "to": "Счет 64686473678894779589",
                }
            ],
        ),
        (empty_file_path, []),
        (wrong_file_path, []),
        (wrong_json_path, []),
    ],
)
def test_get_data_from_json_file(path: str, expected: list) -> None:
    assert get_data_from_json_file(path) == expected
