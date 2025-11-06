import json
from unittest.mock import Mock, patch

from src import get_data_from_json_file


@patch("builtins.open")
def test_get_data_success(mock_open: Mock) -> None:
    """тест успешного чтения и парсинга данных из JSON файла"""
    mock_data = [
        {
            "id": 1,
            "amount": "1000",
            "currency": "USD",
        }
    ]
    json_str = json.dumps(mock_data)
    mock_open.return_value.__enter__.return_value.read.return_value = json_str

    result = get_data_from_json_file("fake_path.json")
    assert result == mock_data


@patch("builtins.open", side_effect=FileNotFoundError)
def test_get_data_file_not_found(mock_open: Mock) -> None:
    """проверка обработки отсутствия файла (исключение FileNotFoundError)"""
    result = get_data_from_json_file("nonexistent.json")
    assert result == []


@patch("builtins.open")
@patch("json.load")
def test_get_data_json_decode_error(mock_json_load: Mock, mock_open: Mock) -> None:
    """проверка обработки ошибки декодирования JSON"""
    mock_json_load.side_effect = json.decoder.JSONDecodeError("Error", "line 1", 0)

    result = get_data_from_json_file("bad_json.json")
    assert result == []
