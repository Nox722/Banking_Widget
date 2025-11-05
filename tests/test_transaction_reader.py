import io
from unittest.mock import Mock, patch

import pandas as pd
from pytest import CaptureFixture

from src import get_data_from_csv_file, get_data_from_excel_file


@patch("builtins.open")
def test_get_data_from_csv_success(mock_open: Mock) -> None:
    """тест успешного чтения данных из файла"""
    csv_content = """id;amount;currency
1;1000;USD
2;2000;EUR
"""
    mock_file = io.StringIO(csv_content)
    mock_open.return_value.__enter__.return_value = mock_file

    expected_data = [
        {"id": "1", "amount": "1000", "currency": "USD"},
        {"id": "2", "amount": "2000", "currency": "EUR"},
    ]

    result = get_data_from_csv_file("fake_path.csv")
    assert result == expected_data


@patch("builtins.open", side_effect=FileNotFoundError)
def test_get_data_from_csv_file_not_found(mock_open: Mock, capfd: CaptureFixture) -> None:
    """проверка обработки отсутствия файла (FileNotFoundError)"""
    result = get_data_from_csv_file("nonexistent.csv")
    assert result == []

    captured = capfd.readouterr()
    assert "Файл не найден. Проверьте указанный путь" in captured.out


@patch("builtins.open", side_effect=Exception)
def test_get_data_from_csv_file_permission_error(mock_open: Mock, capfd: CaptureFixture) -> None:
    """Проверка обработки ошибки считывания файла (любой другой Exception)"""
    result = get_data_from_csv_file("some_file.csv")
    assert result == []

    captured = capfd.readouterr()
    assert "Ошибка при чтении файла" in captured.out


@patch("pandas.read_excel")
def test_get_data_from_excel_success(mock_read_excel: Mock) -> None:
    """тест успешного чтения данных из файла"""
    mock_df = pd.DataFrame({"id": ["1", "2"], "amount": ["1000", "2000"], "currency": ["USD", "EUR"]})

    mock_read_excel.return_value = mock_df

    expected_result = [
        {"id": "1", "amount": "1000", "currency": "USD"},
        {"id": "2", "amount": "2000", "currency": "EUR"},
    ]

    result = get_data_from_excel_file("fake_path.xlsx")
    assert result == expected_result


@patch("pandas.read_excel", side_effect=FileNotFoundError)
def test_get_data_from_excel_file_not_found(mock_read_excel: Mock, capfd: CaptureFixture) -> None:
    """проверка обработки отсутствия файла (FileNotFoundError)"""
    result = get_data_from_excel_file("nonexistent.xlsx")
    assert result == []

    captured = capfd.readouterr()
    assert "Файл не найден. Проверьте указанный путь" in captured.out


@patch("pandas.read_excel", side_effect=Exception)
def test_get_data_from_excel_read_error(mock_read_excel: Mock, capfd: CaptureFixture) -> None:
    """Проверка обработки ошибки считывания файла (любой другой Exception)"""
    result = get_data_from_excel_file("corrupted.xlsx")
    assert result == []

    captured = capfd.readouterr()
    assert "Ошибка при чтении файла:" in captured.out
